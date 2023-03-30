# What

This archive contains firmware for MHB8748 MCU (clone of i8748) that controls
A/D board in the floating part of Metra M1T380 multimeter.

Size: 1024 bytes (complete 8748 ROM)
MD5 checksum: 2a0ef5b134fc4ace8f2af8a0eab639ad

# Disclaimer

I have not attempted to verify dumped firmware by flashing it, but several dumps
have been made with different timings and they all match. Disassembly listing
also looks very promising. Despite this, there is no guarantee that this
firmware is without errors. Use at your own risk.

# Version

i8748 within M1T380 is not labeled with a version number. Therefore, this
archive does not specify a version number. This is contrary to i8080 ROMs in the
same multimeter which always have a version written on their stickers.
Hopefully, this means that only one 8748 ROM version exists in the wild.

# Other notes

The binary has been dumped from a M1T380.1 multimeter with i8080 ROM v3.8,
manufactured in 1990. PN of A/D board is D1791 (low stability version), but
surprisingly enough it uses MAB399 reference, probably due to TKZD13/D zener
shortages they had at the time.

To dump it, 8748 was placed in verification mode by applying +15V to EA pin and
read using ad-hoc Arduino-based "programmer". 8748 remained on D1791 board
during the process, only a couple of traces had to be cut.


Roman Dobrodii `roman ~dot~ dobrodii ~at~ gmail ~dot~ com`
01 June 2022
