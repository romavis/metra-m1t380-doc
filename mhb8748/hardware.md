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
- **0** - ~DATA_OUT (DATA1) output, inverted
- **1** - n/a
- **2** - ~RDY_OUT (RDY1) output, inverted
- **3** - n/a
- **4** - DATA_IN (DATA2) input
- **5** - n/a
- **6** - RDY_IN (RDY2) input
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

## Integrating ADC

Integrating ADC is single-ended with a ground-referenced input. It is built
around analog integrator - I9 opamp with C12 precision polystyrene capacitor
(200.0nF). C12 is charged/discharged by feeding integrator's input from
different current sources which are connected via digitally-controlled
transistor switches:
- **T9 (Sx)** injects current *Ix* proportional to the ADC input voltage
- **T11 (Snul)** discharges integrator capacitor C12, and only opamp offset
  voltage remains on the output.
- **T12 (Sn+)** injects positive calibrated current *+In*.
- **T13 (Sn-)** injects negative calibrated current *-In*.
- **T7 (Sn1+)** injects small positive calibrated current *+In1*.
- **T8 (Sn1-)** injects small negative calibrated current *-In1*.

Currents are determined as follows:
- *Ix* is proportional to the ADC input voltage *Vx* that comes from multiplexer
  I5 via I6 buffer. Current-to-voltage ratio *Ix/Vx* set by R36 is *~55.56
  uA/V*.
- *In* is set by voltage reference I21 (MAB399) or D26 (TKZD13/D) and R25, and
  is in range *670uA~900uA* depending on the reference voltage.
- *In1* is derived from *In* via R33~R35: *In1=In/256*

Integrator output voltage *Vint* is proportional to charge of C12 capacitor
(with negative sign, since it's an inverting integrator):
```
Vint = -INT(I*dt) / C12 = -INT(I*dt) * 5000000 [V/(uA*s)]
```

*Vint* value is continuously monitored by three comparators K0, K1, K2 (MAC111,
clone of LM111).

**NOTE** there is a bug in the manual: K1, K2 are swapped on different diagrams.
We follow this mapping (which agrees with D1639 board block diagram - Obr.19 in
the old manual and Obr.26 in the new one):
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
mainly when multimeter switches ranges and modes (VAC, VDC, IAC, IDC,
calibration..). Therefore, we call this register MREG (*mode register*).

Meanings and combinations of *A[0:2]*, *S[1:29]* signals are documented in the
[modes table](modes.md).

For convenience, we'll call its outputs as MREG Q[31:0], which maps to manual's
signal names as follows (following Verilog-like notation):
```
{S[29:1], A[2:0]} = Q[31:0]
```

MREG is controlled by two signals: R (reset) and WD (write disable). It is worth
noting that reset is **not** always active, and its action depends on WD signal.

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

When MHB8748 is in reset and before firmware begins execution, R and WD pins are
pulled high, so MREG is reset and all its outputs are zero. Since many of those
signals are active-low, driving all of them low indiscriminately turns on most
of relays, which may damage the multimeter if high-voltage or high-current
source is connected to input terminals. This was circumvented by making S[12]
*(+5V RELAY EN)* an active-high signal, which disables drivers of *"critical"*
relays when driven low during MREG reset.
