ADC (D1639)
===========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   adc/mhb8748
..    adc/hardware
..    adc/protocol
..    adc/modes


Metra M1T380 uses integrating ADC made of discrete components. It is located on
D1639 board (or D1791 in low-stability model).

The whole ADC, as well as other parts of analog circuitry, are controlled by
MHB8748 microcontroller (clone of Intel 8748 from MCS-48 family).

This MCU communicates with host Intel 8080 CPU via a custom serial
interface. Since ADC is located in the floating part of the multimeter,
while host CPU is in the grounded part, the interface goes through
optocouplers.

As of April 2023, the firmware of MHB8748, stored in a 1KB on-chip EPROM, has
been dumped, reverse-engineered and documented. For more information see:
:doc:`adc/mhb8748`.
