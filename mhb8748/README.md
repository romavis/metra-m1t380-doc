# MHB8748 reverse-engineering

## Index

- [MHB8748.html](code/MHB8748.html) - Ghidra HTML export of documented firmware
  assembly.
- [MHB8748.bin.gzf](code/MHB8748.bin.gzf) - Ghidra Zip File (imported in Ghidra looks
  way better than HTML).
- [hardware.md](hardware.md) - description of hardware surrounding MHB8748 chip.
- [protocol.md](protocol.md) - serial protocol description
  
## Role

In Metra M1T380, MHB8748 is used to control analog circuitry, which is basically
an integrating ADC with resistor dividers and various amplifiers.

It is located on board D1639 (D1791) and has designator I14.

In particular:
1. Handles communication with main CPU through optically isolated bidirectional
   serial interface.
2. Controls relays and MOS switches that control analog signal routing.
3. Monitors integrating ADC comparator outputs.
4. Acts as a counter for integrating ADC.
5. Monitors AC 50Hz/60Hz sinewave to synchronize measurements with the period of
   mains clock, in an attempt to filter 50Hz component from the measurement
   result thanks to averaging over whole number of periods.

## Highlights

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