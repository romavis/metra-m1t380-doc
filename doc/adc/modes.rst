# Modes

- [Mode 0](#mode-0): VDC 150 mV
- [Mode 1](#mode-1): VDC 1.5 V
- [Mode 2](#mode-2): VDC 15 V
- [Mode 3](#mode-3): VDC 150 V
- [Mode 4](#mode-4): VDC 1500 V
- [Mode 5](#mode-5): IDC 15 mA
- [Mode 6](#mode-6): IDC 1.5 A
- [Mode 7](#mode-7): OHMS 150 Ω
- [Mode 8](#mode-8): OHMS 1.5 kΩ
- [Mode 9](#mode-9): OHMS 15 kΩ
- [Mode 10](#mode-10): OHMS 150 kΩ
- [Mode 11](#mode-11): OHMS 1.5 MΩ
- [Mode 12](#mode-12): OHMS 15 MΩ
- [Mode 13](#mode-13): VAC 150 mV
- [Mode 14](#mode-14): VAC 1.5 V
- [Mode 15](#mode-15): VAC 15 V
- [Mode 16](#mode-16): VAC 150 V
- [Mode 17](#mode-17): VAC 1500 V
- [Mode 18](#mode-18): IAC 15 mA
- [Mode 19](#mode-19): IAC 1.5 A
- [Mode 20](#mode-20): Cal AC/DC zero
- [Mode 21](#mode-21): Cal AC/DC -5Vref
- [Mode 22](#mode-22): Cal meas -5Vref
- [Mode 23](#mode-23): Cal DIV zero
- [Mode 24](#mode-24): Cal DIV CAL+
- [Mode 25](#mode-25): Cal DIV Izero
- [Mode 26](#mode-26): Cal ADC zero
- [Mode 27](#mode-27): Cal ADC CAL+
- [Mode 28](#mode-28): Cal ADC CAL-

**NOTE** - in this document we use following symbols to mark special or variable states:
 - **fil** - MREG bit is equal to `fil` parameter of *set_mode* command.
 - **K** - MREG bit value is unchanged by *set_mode* - so it keeps its value that it had before *set_mode* command was executed.
 - **CF** - if current source was enabled prior to entering this mode (Re6~9 @ D1642 were on), Re2 @ D1639 will be switched off; otherwise behaves like `fil`.
 - **CS** - if one of Re13,14 was enabled prior to entering this mode, both Re13,14 will be turned on, disconnecting input terminals H:L from the current shunts and shorting them through diodes D5,D6.

## Overview table

|        |A0 |A1 |A2 |S1 |S2 |S3 |S4 |S5 |S6 |S7 |S8 |S9 |S10|S11|S12|S13|S14|S15|S16|S17|S18|S19|S20|S21|S22|S23|S24|S25|S26|S27|S28|S29|
| :-:    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|mode0  |0  |0  |0  |1  |0  |0  |0  |1  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode1  |0  |0  |0  |0  |1  |0  |0  |1  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode2  |0  |0  |0  |0  |0  |1  |0  |1  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode3  |0  |0  |0  |0  |1  |0  |0  |0  |fil|1  |1  |1  |1  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode4  |0  |0  |0  |0  |0  |1  |0  |0  |fil|1  |1  |1  |1  |1  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode5  |0  |0  |0  |1  |0  |0  |0  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode6  |0  |0  |0  |1  |0  |0  |0  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode7  |1  |0  |0  |0  |1  |0  |0  |1  |fil|0  |1  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode8  |1  |0  |0  |0  |1  |0  |0  |1  |fil|1  |0  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode9  |1  |0  |0  |0  |0  |1  |0  |1  |fil|1  |0  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode10 |1  |0  |0  |0  |0  |1  |0  |1  |fil|1  |1  |0  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode11 |1  |0  |0  |0  |0  |1  |0  |1  |fil|1  |1  |1  |0  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode12 |1  |0  |0  |0  |0  |1  |0  |1  |fil|1  |1  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode13 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |1  |0  |1  |1  |0  |1  |1  |0  |fil|
|mode14 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |1  |0  |1  |0  |0  |0  |1  |0  |fil|
|mode15 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |0  |1  |0  |0  |1  |0  |1  |1  |1  |0  |fil|
|mode16 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |0  |1  |0  |0  |1  |0  |0  |0  |0  |1  |fil|
|mode17 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |1  |0  |1  |1  |0  |0  |1  |0  |1  |fil|
|mode18 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |1  |1  |0  |0  |1  |1  |0  |1  |1  |0  |fil|
|mode19 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |0  |1  |1  |0  |0  |1  |1  |0  |1  |1  |0  |fil|
|mode20 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |CS |CS |1  |1  |1  |0  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode21 |0  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |CS |CS |1  |1  |1  |0  |0  |1  |0  |0  |1  |0  |0  |fil|
|mode22 |1  |1  |0  |0  |0  |0  |1  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |CS |CS |1  |1  |1  |0  |0  |1  |0  |0  |1  |0  |0  |fil|
|mode23 |1  |1  |1  |1  |0  |0  |0  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |CS |CS |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode24 |1  |0  |0  |1  |0  |0  |0  |0  |fil|1  |1  |1  |1  |1  |1  |0  |1  |0  |CS |CS |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode25 |0  |0  |0  |1  |0  |0  |0  |0  |fil|1  |1  |1  |1  |1  |1  |1  |1  |1  |CS |CS |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |fil|
|mode26 |0  |0  |1  |K  |K  |K  |K  |K  |CF |K  |K  |K  |K  |1  |1  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |
|mode27 |1  |0  |1  |K  |K  |K  |K  |K  |CF |K  |K  |K  |K  |1  |1  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |
|mode28 |0  |1  |1  |K  |K  |K  |K  |K  |CF |K  |K  |K  |K  |1  |1  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |

## Mode 0

VDC 150 mV

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |1   |0   |0   |0   |1   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|1|fil|
|ON|OFF|OFF|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin / 2
    [(A0,A1,A2) = (0,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-100 (T3 on)
    [(S1,S2,S3,S4) = (1,0,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 1

VDC 1.5 V

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |0   |1   |0   |0   |1   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|0|0|1|fil|
|OFF|ON|OFF|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin / 2
    [(A0,A1,A2) = (0,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-10 (T4 on)
    [(S1,S2,S3,S4) = (0,1,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 2

VDC 15 V

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |0   |0   |1   |0   |1   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|fil|
|OFF|OFF|ON|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin / 2
    [(A0,A1,A2) = (0,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-1 (T5 on)
    [(S1,S2,S3,S4) = (0,0,1,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 3

VDC 150 V

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |0   |1   |0   |0   |0   |fil |1   |1   |1   |1   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|0|0|0|fil|
|OFF|ON|OFF|OFF|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|0|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin / 2
    [(A0,A1,A2) = (0,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-10 (T4 on)
    [(S1,S2,S3,S4) = (0,1,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider connected to H terminal
    [(S13,S14,S15) = (0,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 4

VDC 1500 V

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |0   |0   |1   |0   |0   |fil |1   |1   |1   |1   |1   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|0|fil|
|OFF|OFF|ON|OFF|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|0|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|ON|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin / 2
    [(A0,A1,A2) = (0,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-1 (T5 on)
    [(S1,S2,S3,S4) = (0,0,1,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider connected to H1KV terminal
    [(S13,S14,S15) = (1,0,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 5

IDC 15 mA

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |1   |0   |0   |0   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|fil|
|ON|OFF|OFF|OFF|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|0|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|ON|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin / 2
    [(A0,A1,A2) = (0,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-100 (T3 on)
    [(S1,S2,S3,S4) = (1,0,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are connected to 10 Ω shunt
    [(S16,S17) = (0,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 6

IDC 1.5 A

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |1   |0   |0   |0   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|fil|
|ON|OFF|OFF|OFF|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|0|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|ON|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin / 2
    [(A0,A1,A2) = (0,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-100 (T3 on)
    [(S1,S2,S3,S4) = (1,0,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are connected to 0.1 Ω shunt
    [(S16,S17) = (1,0)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 7

OHMS 150 Ω

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |1   |0   |0   |1   |fil |0   |1   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|0|0|1|fil|
|OFF|ON|OFF|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|1|1|0|1|1|1|1|1|1|
|ON|OFF|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin
    [(A0,A1,A2) = (1,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: none
    [(A0,A1,A2) = (1,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-10 (T4 on)
    [(S1,S2,S3,S4) = (0,1,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source connected, Hx:Lx or H:L selected via OHMS 2-4 switch
    [(S11) = (0)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 5 mA (Re1,2 on)
    [(S7,S8,S9,S10) = (0,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 8

OHMS 1.5 kΩ

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |1   |0   |0   |1   |fil |1   |0   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|0|0|1|fil|
|OFF|ON|OFF|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|1|1|1|1|1|1|
|OFF|ON|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin
    [(A0,A1,A2) = (1,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: none
    [(A0,A1,A2) = (1,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-10 (T4 on)
    [(S1,S2,S3,S4) = (0,1,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source connected, Hx:Lx or H:L selected via OHMS 2-4 switch
    [(S11) = (0)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 mA (Re3 on)
    [(S7,S8,S9,S10) = (1,0,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 9

OHMS 15 kΩ

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |0   |1   |0   |1   |fil |1   |0   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|fil|
|OFF|OFF|ON|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|1|1|1|1|1|1|
|OFF|ON|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin
    [(A0,A1,A2) = (1,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: none
    [(A0,A1,A2) = (1,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-1 (T5 on)
    [(S1,S2,S3,S4) = (0,0,1,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source connected, Hx:Lx or H:L selected via OHMS 2-4 switch
    [(S11) = (0)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 mA (Re3 on)
    [(S7,S8,S9,S10) = (1,0,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 10

OHMS 150 kΩ

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |0   |1   |0   |1   |fil |1   |1   |0   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|fil|
|OFF|OFF|ON|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|0|1|0|1|1|1|1|1|1|
|OFF|OFF|ON|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin
    [(A0,A1,A2) = (1,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: none
    [(A0,A1,A2) = (1,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-1 (T5 on)
    [(S1,S2,S3,S4) = (0,0,1,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source connected, Hx:Lx or H:L selected via OHMS 2-4 switch
    [(S11) = (0)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 50 uA (Re4 on)
    [(S7,S8,S9,S10) = (1,1,0,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 11

OHMS 1.5 MΩ

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |0   |1   |0   |1   |fil |1   |1   |1   |0   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|fil|
|OFF|OFF|ON|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|0|0|1|1|1|1|1|1|
|OFF|OFF|OFF|ON|ON|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin
    [(A0,A1,A2) = (1,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: none
    [(A0,A1,A2) = (1,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-1 (T5 on)
    [(S1,S2,S3,S4) = (0,0,1,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source connected, Hx:Lx or H:L selected via OHMS 2-4 switch
    [(S11) = (0)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 5 uA (Re5 on)
    [(S7,S8,S9,S10) = (1,1,1,0)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 12

OHMS 15 MΩ

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |0   |1   |0   |1   |fil |1   |1   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|fil|
|OFF|OFF|ON|OFF|ON||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|0|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin
    [(A0,A1,A2) = (1,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: none
    [(A0,A1,A2) = (1,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-1 (T5 on)
    [(S1,S2,S3,S4) = (0,0,1,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes directly from H terminal
    [(S5) = (1)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source connected, Hx:Lx or H:L selected via OHMS 2-4 switch
    [(S11) = (0)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 13

VAC 150 mV

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |1   |0   |1   |1   |0   |1   |1   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|0|1|0|fil|
|ON|ON|OFF|ON|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: H -> I1; L -> GND
    [(S18,S19,S20,S21,S22) = (0,1,0,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: I1 out (H/F1 voltage x3.0)
    [(S24,S25) = (1,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: I2 out (see I2 input routing above)
    [(S26,S27,S28) = (1,1,0)]

```

## Mode 14

VAC 1.5 V

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |1   |0   |1   |0   |0   |0   |1   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|0|1|0|fil|
|ON|ON|OFF|ON|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: H -> I1; L -> GND
    [(S18,S19,S20,S21,S22) = (0,1,0,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: I1 out (H/F1 voltage x3.0)
    [(S26,S27,S28) = (0,1,0)]

```

## Mode 15

VAC 15 V

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |0   |1   |0   |0   |1   |0   |1   |1   |1   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|1|0|0|fil|
|ON|ON|ON|OFF|ON|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: H -> I8;  F1 -> I1; L -> GND
    [(S18,S19,S20,S21,S22) = (0,0,1,0,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: I8 out (H voltage x0.03)
    [(S24,S25) = (0,1)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: I2 out (see I2 input routing above)
    [(S26,S27,S28) = (1,1,0)]

```

## Mode 16

VAC 150 V

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |0   |1   |0   |0   |1   |0   |0   |0   |0   |1   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|1|0|0|fil|
|ON|ON|ON|OFF|ON|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: H -> I8;  F1 -> I1; L -> GND
    [(S18,S19,S20,S21,S22) = (0,0,1,0,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: I8 out (H voltage x0.03)
    [(S26,S27,S28) = (0,0,1)]

```

## Mode 17

VAC 1500 V

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |1   |0   |1   |1   |0   |0   |1   |0   |1   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|1|fil|
|ON|ON|OFF|OFF|ON|ON||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are not connected to current shunts
    [(S16,S17) = (1,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: H1KV -> I11;  F1 -> I1; L -> GND
    [(S18,S19,S20,S21,S22) = (0,1,1,0,1)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: I11 out (H1KV voltage x0.003)
    [(S26,S27,S28) = (1,0,1)]

```

## Mode 18

IAC 15 mA

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |1   |1   |0   |0   |1   |1   |0   |1   |1   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|0|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|ON|OFF|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|0|fil|
|ON|ON|OFF|OFF|ON|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are connected to 10 Ω shunt
    [(S16,S17) = (0,1)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: F1 -> I1; L -> GND
    [(S18,S19,S20,S21,S22) = (0,1,1,0,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: I1 out (H/F1 voltage x3.0)
    [(S24,S25) = (1,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: I2 out (see I2 input routing above)
    [(S26,S27,S28) = (1,1,0)]

```

## Mode 19

IAC 1.5 A

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |0   |1   |1   |0   |0   |1   |1   |0   |1   |1   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|0|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|ON|

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|0|fil|
|ON|ON|OFF|OFF|ON|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    SELECTED: H:L are connected to 0.1 Ω shunt
    [(S16,S17) = (1,0)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: F1 -> I1; L -> GND
    [(S18,S19,S20,S21,S22) = (0,1,1,0,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: I1 out (H/F1 voltage x3.0)
    [(S24,S25) = (1,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: I2 out (see I2 input routing above)
    [(S26,S27,S28) = (1,1,0)]

```

## Mode 20

Cal AC/DC zero

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |CS  |CS  |1   |1   |1   |0   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|CS|CS|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|0|0|fil|
|ON|OFF|OFF|OFF|ON|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (CS,CS)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: F1 -> I1;  but L is disconnected!
    [(S18,S19,S20,S21,S22) = (1,1,1,0,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 21

Cal AC/DC -5Vref

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |CS  |CS  |1   |1   |1   |0   |0   |1   |0   |0   |1   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|CS|CS|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|0|0|fil|
|ON|OFF|OFF|OFF|ON|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC1 (ADC measures AC/DC converter RMS out)
    [(A0,A1,A2) = (0,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (CS,CS)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: F1 -> I1;  but L is disconnected!
    [(S18,S19,S20,S21,S22) = (1,1,1,0,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: -5V ref
    [(S26,S27,S28) = (1,0,0)]

```

## Mode 22

Cal meas -5Vref

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |1   |0   |0   |0   |0   |1   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |CS  |CS  |1   |1   |1   |0   |0   |1   |0   |0   |1   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|fil|
|OFF|OFF|OFF|ON|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|CS|CS|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|0|0|fil|
|ON|OFF|OFF|OFF|ON|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: AC2 (ADC measures AC/DC converter's -5V ref voltage)
    [(A0,A1,A2) = (1,1,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (1,1,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp off (T6 on)
    [(S1,S2,S3,S4) = (0,0,0,1)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (CS,CS)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: F1 -> I1;  but L is disconnected!
    [(S18,S19,S20,S21,S22) = (1,1,1,0,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: -5V ref
    [(S26,S27,S28) = (1,0,0)]

```

## Mode 23

Cal DIV zero

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |1   |1   |1   |0   |0   |0   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |CS  |CS  |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|fil|
|ON|OFF|OFF|OFF|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|CS|CS|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin
    [(A0,A1,A2) = (1,1,1)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (1,1,1)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-100 (T3 on)
    [(S1,S2,S3,S4) = (1,0,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (CS,CS)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 24

Cal DIV CAL+

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |1   |0   |0   |0   |0   |fil |1   |1   |1   |1   |1   |1   |0   |1   |0   |CS  |CS  |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|fil|
|ON|OFF|OFF|OFF|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|0|1|0|CS|CS|
|OFF|OFF|OFF|OFF|OFF|ON|ON|OFF|ON|||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin
    [(A0,A1,A2) = (1,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: none
    [(A0,A1,A2) = (1,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-100 (T3 on)
    [(S1,S2,S3,S4) = (1,0,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider connected to CAL+:CAL- source
    [(S13,S14,S15) = (0,1,0)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (CS,CS)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 25

Cal DIV Izero

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |1   |0   |0   |0   |0   |fil |1   |1   |1   |1   |1   |1   |1   |1   |1   |CS  |CS  |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |fil |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|fil|
|ON|OFF|OFF|OFF|OFF||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|CS|CS|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|fil|
|ON|OFF|OFF|OFF|OFF|OFF||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: k * Vin / 2
    [(A0,A1,A2) = (0,0,0)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,0)]

D1639 - T3~6 - controls input amplifier gain
    SELECTED: input amp k=-100 (T3 on)
    [(S1,S2,S3,S4) = (1,0,0,0)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    SELECTED: Vin comes from H1 (from input voltage divider or current shunt)
    [(S5) = (0)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    SELECTED: input voltage divider disconnected
    [(S13,S14,S15) = (1,1,1)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (CS,CS)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    SELECTED: Imeas = 0.5 uA (Re1~5 off)
    [(S7,S8,S9,S10) = (1,1,1,1)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    SELECTED: AC/DC converter disconnected from all input terminals
    [(S18,S19,S20,S21,S22) = (1,1,1,1,0)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    SELECTED: GND
    [(S24,S25) = (0,0)]

D1638 - I5 - selects input to I9 (RMS converter)
    SELECTED: GND
    [(S26,S27,S28) = (0,0,0)]

```

## Mode 26

Cal ADC zero

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |1   |K   |K   |K   |K   |K   |CF  |K   |K   |K   |K   |1   |1   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|K|CF|
|||||||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|1|1|K|K|K|K|K|
|||||OFF|ON||||||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|K|K|K|K|K|K|
|ON|||||||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: GND
    [(A0,A1,A2) = (0,0,1)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (0,0,1)]

D1639 - T3~6 - controls input amplifier gain
    [(S1,S2,S3,S4) = (K,K,K,K)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    [(S5) = (K)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    [(S13,S14,S15) = (K,K,K)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (K,K)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    [(S7,S8,S9,S10) = (K,K,K,K)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    [(S18,S19,S20,S21,S22) = (K,K,K,K,K)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    [(S24,S25) = (K,K)]

D1638 - I5 - selects input to I9 (RMS converter)
    [(S26,S27,S28) = (K,K,K)]

```

## Mode 27

Cal ADC CAL+

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |1   |K   |K   |K   |K   |K   |CF  |K   |K   |K   |K   |1   |1   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|K|CF|
|||||||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|1|1|K|K|K|K|K|
|||||OFF|ON||||||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|K|K|K|K|K|K|
|ON|||||||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: CAL+
    [(A0,A1,A2) = (1,0,1)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL-
    [(A0,A1,A2) = (1,0,1)]

D1639 - T3~6 - controls input amplifier gain
    [(S1,S2,S3,S4) = (K,K,K,K)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    [(S5) = (K)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    [(S13,S14,S15) = (K,K,K)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (K,K)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    [(S7,S8,S9,S10) = (K,K,K,K)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    [(S18,S19,S20,S21,S22) = (K,K,K,K,K)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    [(S24,S25) = (K,K)]

D1638 - I5 - selects input to I9 (RMS converter)
    [(S26,S27,S28) = (K,K,K)]

```

## Mode 28

Cal ADC CAL-

**MREG signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |1   |K   |K   |K   |K   |K   |CF  |K   |K   |K   |K   |1   |1   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |

**Board D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|K|CF|
|||||||

**Board D1642 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|1|1|K|K|K|K|K|
|||||OFF|ON||||||

**Board D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|K|K|K|K|K|K|
|ON|||||||

**State decoding**

```
D1639 - I5 - selects signal that goes to ADC input
    SELECTED: CAL-
    [(A0,A1,A2) = (0,1,1)]

D1639 - I4 - grounds selected signal on ADC board
    SELECTED: CAL+
    [(A0,A1,A2) = (0,1,1)]

D1639 - T3~6 - controls input amplifier gain
    [(S1,S2,S3,S4) = (K,K,K,K)]

D1639 - Re1 - takes Vin either from H or from H1 terminal
    [(S5) = (K)]

D1642 - Re10~12 - connects and disconnects sources to input divider
    [(S13,S14,S15) = (K,K,K)]

D1642 - Re13,14 - connects and disconnects current shunt resistors
    [(S16,S17) = (K,K)]

D1642 - Re6~9 - connects current source to Hx:Lx or H:L terminals
    SELECTED: current source disconnected
    [(S11) = (1)]

D1642 - Re1~5 - controls Hx-Lx current source for OHMS measurement
    [(S7,S8,S9,S10) = (K,K,K,K)]

D1638 - Re1~5 - connects and disconnects AC/DC converter inputs
    [(S18,S19,S20,S21,S22) = (K,K,K,K,K)]

D1638 - I4 - selects input to I2 (x10 amplifier)
    [(S24,S25) = (K,K)]

D1638 - I5 - selects input to I9 (RMS converter)
    [(S26,S27,S28) = (K,K,K)]

```

