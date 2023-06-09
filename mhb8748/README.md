# MHB8748 reverse-engineering

## Index

- [MHB8748.html](code/MHB8748.html) - Ghidra HTML export of documented firmware
  assembly.
- [MHB8748.bin.gzf](code/MHB8748.bin.gzf) - Ghidra Zip File (imported in Ghidra looks
  way better than HTML).
- [hardware.md](hardware.md) - description of hardware surrounding MHB8748 chip.
- [protocol.md](protocol.md) - serial protocol description.
- [modes.md](modes.md) - auto-generated listing of measurement modes supported
  by M1T380.
  
## Role

In Metra M1T380, MHB8748 (I14 on board D1639) is an MCU located in the floating
part of the multimeter. It is responsible for:
1. Handles communication with main CPU through optically isolated bidirectional
   half-duplex serial interface.
2. Loads MREG (*mode register*) that controls relays and MOS switches which
   determine analog signal routing on all analog boards (D1639, D1642, D1638).
3. Implements all digital logic of the multi-slope integrating ADC: controls MOS
   switches, monitors analog comparator outputs and counts time spent in
   different ramp phases.
4. Monitors AC 50Hz/60Hz sinewave to synchronize measurements with the period of
   the mains, in an attempt to remove periodic mains component from the
   measurement thanks to averaging over a whole number of mains periods.

## Highlights

- 1 KByte UV-erasable ROM
- 64 byte RAM (general-purpose registers are part of this space). 
- XTAL oscillator.
- P1, P2: two 8-bit quasi-bidirectional IO ports (open drain with pull-high
  accelerator).
- BUS: 8-bit in/out/hi-Z port with RD, WR strobes. 
- Built-in 8-bit timer - which is not used in M1T380.
- External interrupt pin - which is not used in M1T380.
- Interrupt-less and timer-less firmware which does all IO by bitbanging; time
  measurement is done by counting number of iterations of carefully-timed
  program loops.