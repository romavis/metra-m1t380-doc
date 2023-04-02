# MHB8748 serial protocol

MHB8748 MCU communicates with host CPU using custom asyncrhonous serial
interface that consits of 4 signals.

## Signaling

Tx channel - for transmission to host CPU:
- DATA1 - MHB's output DATA_OUT
- RDY2 - MHB's input RDY_IN

Rx channel - for reception from host CPU:
- DATA2 - MHB's input DATA_IN
- RDY1 - MHB's output RDY_OUT

Same properties apply to both channels:
- Unidirectional
- Asyncrhonous (as there is no separate CLK line)
- Bit clock is fixed at 10000 bits/s
- Byte-oriented
- Transmit 1 byte at a time
- MSB is transmitted first

Each channel is composed of two signals:
- DATA - used by transmitter to alert receiver that data is available for
  transmission, precisely marks start of transmission, transmits data bits
- RDY - used by receiver to acknowledge readiness to receive

That's how a transmission of a single byte looks like:
![waveform](img/serial.svg)

Transmission consists of a few steps:
1. Idle bus state is DATA=1, RDY=1.
2. Transmitter sets DATA=0 to alert receiver that there is data available, and
   waits for RDY to go low.
3. After unspecified time, receiver notices that DATA==0, sets RDY=0, and starts
   closely watching state of DATA line.
4. When transmitter sees that RDY==0, it quickly (within a few tens of
   microseconds) sets DATA==1 and starts timer that fires with period of 100 us.
   Each time the timer fires, transmitter shifts consequtive bit of data to the
   DATA line, starting from MSB (D7) and ending with LSB (D0).  
5. Receiver sees that DATA==1 and counts 150 us. After 150 us have elapsed, it
   samples DATA line - that will be bit D7. Then receiver starts timer that
   fires with period of 100 us. Each time the timer fires, receiver samples DATA
   line and reads next data bit from it - starting from D6 and till D0.
6. After transmitter shifts out D0 onto data line, it waits for 100 us, and sets
   DATA=1 (bus idle). Transmission is complete.
7. After receiver has sampled the final D0 bit, it sets RDY=1. Reception is
   complete.
8. Bus is idle (DATA=1, RDY=1), so a new transmission can be started.


**NOTES**:
1. Exact time when RDY goes high at the end of transmission is irrelevant - but
   it is crucial that when transmitter begins transmitting next byte the bus is
   already in the idle state (RDY=1, DATA=1), so it's best if receiver does it
   before or at the moment of sampling the last bit.

## Software protocol

Most of the time, MHB8748 busy-loops in the main loop, waiting for data from
host. Host communicates with MHB8748 by sending a single command byte. MHB8748
executes that command, in some cases tries to send some data bytes back to host
as a result, and returns back to the main loop, waiting for next command.
Exception to this are the factory test procedures, which, when executed, may run
their own infinite loops that sometimes require special sequences to break out
and get back into the main loop.

**Failsafe**

MHB8748 firmware implements a failsafe mechanism: whenever host CPU has data to
send (DATA_IN==0), it makes MHB8748 break out of most of the loops, do a
soft-reset and accept host's command.

However, this will **not** work to break out of ADC integration procedures. So
if ADC hardware is malfunctioning, making MHB8748 to loop endlessly waiting for
some hardware condition, it will appear stuck till MHB8748 is hard-reset. This
also means that it is, unfortunately, not possible to terminate ADC conversion
before it finishes, even if it's the longest one (2~3 sec).

## Commands

**NOTE:** whenever we say "x" in binary notation, that means that the value of
the bit is irrelevant. Usually you would write 0 there.

### set_mode

Sets MREG register, which controls analog signal routing and operation modes
of amplifiers, converters, range selectors, etc.

Command byte:
| cmd[7] | cmd[6] | cmd[5] | cmd[4] | cmd[3] | cmd[2] | cmd[1] | cmd[0] |
|--------|--------|--------|--------|--------|--------|--------|--------|
|   0    |  x     |   fil  | mode[4]| mode[3]| mode[2]| mode[1]| mode[0]|

- **fil** - 1 to enable filter, 0 to disable filter
- **mode** - index of a mode

For documentation on each mode, see [Modes](#modes).

### run_meas

Executes one ADC conversion, which means running through:
- T1 phase - integrating input voltage
- T2 phase - down-run using high calibrated current (only for large input
  voltages)
- T3 phase - down-run using small calibrated current
- Postprocessing of results
- Sending back result of the measurement to the host

Command byte:
| cmd[7] | cmd[6] | cmd[5] | cmd[4] | cmd[3] | cmd[2] | cmd[1] | cmd[0] |
|--------|--------|--------|--------|--------|--------|--------|--------|
|   1    |   0    |   0    |   0    |   0    |  dur[2]| dur[1] | dur[0] |

- **dur** - specifies duration of T1 phase:
  - *3'bxx1* - 1 mains period (e.g. 20ms for 50Hz, 16.7ms for 60Hz)
  - *3'bx10* - 10 mains periods (e.g. 200ms for 50Hz, 166.7ms for 60Hz)
  - *3'bx00* - 100 mains periods (e.g. 2000ms for 50Hz, 1666.7ms for 60Hz)

Format of the results:
**TBD**

### run_test

Executes one of factory testing subroutines which are there to aid in
validation, adjustments and repairs of D1639 board.

Command byte:
| cmd[7] | cmd[6] | cmd[5] | cmd[4] | cmd[3] | cmd[2] | cmd[1] | cmd[0] |
|--------|--------|--------|--------|--------|--------|--------|--------|
|   1    | test[3]|test[2] | test[1]| test[0]|   x    |   x    |   x    |

- **test** - select test program:
  - *0* - invalid value (command will be interpreted as **run_meas**) 
  - *1* - test_comm
  - *2* - test_mode26_Snul
  - *3* - test_Snp_Snn_switches
  - *4* - test_Sn1p_Sn1n_switches
  - *5* - test_comparator_K1
  - *6* - test_comparator_K2
  - *7* - test_mode27_28_Sx_Snul
  - Other values - same as *7*

Each test has its own program, see [Tests](#tests).

## Modes

**TBD**

## Tests

**TBD**
