# Role

In Metra M1T380, MHB8748 is used to control analog circuitry, which is basically
an integrating ADC with resistor dividers and various amplifiers.

It is located on board D1639 (D1791) and has designator I14.

In particular:
1. Handles communication with main CPU through optically isolated bidirectional
   serial interface.
2. Controls relays and MOS switches that control analog signal routing.
3. Monitors analog comparator outputs.
4. Acts as a counter for integrating ADC using its built-in timer synchronized
   by crystal oscillator.
5. Monitors AC 50Hz/60Hz sinewave to synchronize measurements with the period of
   mains clock, in an attempt to filter 50Hz component from the measurement
   result thanks to averaging over whole number of periods.

# Highlights

- 1 KByte UV-erasable ROM
- 64 byte RAM (general-purpose registers are part of this space). 
- XTAL oscillator.
- 3 interrupt vectors: RESET, external INT pin, and internal TIMER.
- INT: external active-low level-sensitive interrupt request pin.
- TCNT: 8-bit timer that can be clocked from system XTAL (fixed clock:
  *Fosc/480*) or from external T1 pin, and generates an interrupt on overflow.
- P1, P2: two 8-bit quasi-bidirectional IO ports (open drain with pull-high
  accelerator).
- BUS: 8-bit in/out/hi-Z port with RD, WR strobes. 
- Support for external memory.

# D1639 board description

**NOTE:** register formed from 4x MHB4099 chips (I16~I19 on D1639) will be
called MREG in this document (*mode register*).

## MCU

XTAL oscillator in M1T380 is **6.0 MHz**. This gives us following clocks in the
system:
- State clock: **2 MHz** (can be routed out to T0 pin).
- Cycle clock: **400 kHz**.
- A simple 1-cycle instruction such as *NOP* takes exactly **2.5 us**. 
- Timer clock: **12.5 kHz**.

Port P1 usage:
- **0** - serial ~DATA_OUT (DATA1), signal inverted
- **1** - n/a
- **2** - serial ~RDY_OUT (RDY1), signal inverted
- **3** - n/a
- **4** - serial DATA_IN (DATA2), non-inverted
- **5** - n/a
- **6** - serial RDY_IN (RDY2), non-inverted
- **7** - 50Hz/60Hz mains clock input (*SINE*)

Port P2 usage:
- **0** - controls T9 (*Sx*)
- **1** - controls T12 (*Sn+*)
- **2** - controls T7 (*Sn1+*)
- **3** - controls T13 (*Sn-*)
- **4** - controls T8 (*Sn1-*)
- **5** - controls T11 (*Snul*)
- **6** - n/a
- **7** - MREG R

BUS port usage:
- **BUS[2:0]** - MREG ADDR[2:0]
- **BUS[6:3]** - MREG DATA[3:0]
- **BUS[7]** - MREG WD (*write disable*)

Other inputs:
- **INT** - comparator K1 output
- **T0** - comparator K2 output
- **T1** - comparator K0 output

## Comparators K0,K1,K2

These are MAC111 (clone of LM111) comparators that monitor ADC integrator output
voltage (*Vint*).

**NOTE** there is a bug in the manual: K1, K2 are swapped on different diagrams.
We follow this mapping (which agrees with D1639 board block diagram given in the
manual):
- K0 is I12
- K1 is I11
- K2 is I13

### K0

K0 watches over polarity of ADC integrator output by comparing it to 0V. It is
inverting:
- Positive integrator output (**negative ADC input voltage**) -> T1 pin is
  **LOW**
- Negative integrator output (**positive ADC input voltage**) -> T1 pin is
  **HIGH**

Jump instructions behave like this:
- **JT1** jumps if *Vint* is **negative**
- **JNT1** jumps if *Vint* is **positive**

### K1

K1 is an out-of-range detector:
- Integrator output within *[-Uk1, Uk1]* range -> INT pin is **LOW**
- Integrator output out of range -> INT pin is **HIGH**

Jump instructions behave like this:
- **JNI** jumps if *Vint* is **within** *[-Uk1, Uk1]* range
 
*Uk1* is about 9V. Due to how integrating ADC works, the exact value of this
threshold is not important.

### K2

K2 is an out-of-range detector:
- Integrator output within *[-Uk2, Uk2]* range -> T0 pin is **LOW**
- Integrator output out of range -> T0 pin is **HIGH**

Jump instructions behave like this:
- **JT0** jumps if *Vint* is **out** of *[-Uk2, Uk2]* range
- **JNT0** jumps if *Vint* is **within** *[-Uk2, Uk2]* range
  
Due to approx. x30 voltage amplification by I10, effective K2's threshold
  *Uk2* is approximately 30 times lower than *Uk1*, about 300mV. Due to how
  integrating ADC works, the exact value of this threshold is not important.

## MREG

I16~I19 acts as a 32-bit output-only register. Outputs of this register control
various analog routing switches, relays and muxes in the multimeter, and are
called *A[0:2]*, *S[1:29]* in the user's manual. They do not change often -
mainly when multimeter switches modes (VAC, VDC, IAC, IDC, calibration..) or
input ranges. Therefore, we call this register MREG (*mode register*).

For convenience, we'll call its outputs as MREG Q[31:0], which maps to manual's
signal names as follows (following Verilog-like notation):
```
{S[29:1], A[2:0]} = Q[31:0]
```

MREG is controlled by two signals: R (reset) and WD (write disable). It is worth
noting that reset is **not** always active, and its action depends on WD state.

MREG mode is determined as follows:

| R  | WD | Mode    | Addressed Q[n] | Other Q[n]     |
|----|----|---------|----------------|----------------|
| 0  | 0  | write   | DATA[m]        | previous value |
| 0  | 1  | storage | previous value | previous value |
| 1  | 0  | demux   | DATA[m]        | 0              |
| 1  | 1  | reset   | 0              | 0              |

In write and demux modes, four *Q[n]* outputs are addressed according to
value on *ADDR[]* inputs and are mapped to four *DATA[n]* inputs as follows:
```
Q[ADDR]    = DATA[0]
Q[ADDR+8]  = DATA[1]
Q[ADDR+16] = DATA[2]
Q[ADDR+24] = DATA[3]
```
The other 28 *Q[n]* outputs either keep their previous state (in write mode) or
are set to 0 (in demux mode).

