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
- [Mode 20](#mode-20): Cal AC/DC 1
- [Mode 21](#mode-21): Cal AC/DC 2
- [Mode 22](#mode-22): Cal AC/DC mer u
- [Mode 23](#mode-23): Cal DIV zero
- [Mode 24](#mode-24): Cal DIV cal
- [Mode 25](#mode-25): Cal I zero
- [Mode 26](#mode-26): Cal ADC GND
- [Mode 27](#mode-27): Cal ADC CAL+
- [Mode 28](#mode-28): Cal ADC CAL-

## Overview table

|        |A0 |A1 |A2 |S1 |S2 |S3 |S4 |S5 |S6 |S7 |S8 |S9 |S10|S11|S12|S13|S14|S15|S16|S17|S18|S19|S20|S21|S22|S23|S24|S25|S26|S27|S28|S29|
| :-:    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|mode   0|0  |0  |0  |1  |0  |0  |0  |1  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   1|0  |0  |0  |0  |1  |0  |0  |1  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   2|0  |0  |0  |0  |0  |1  |0  |1  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   3|0  |0  |0  |0  |1  |0  |0  |0  |F  |1  |1  |1  |1  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   4|0  |0  |0  |0  |0  |1  |0  |0  |F  |1  |1  |1  |1  |1  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   5|0  |0  |0  |1  |0  |0  |0  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   6|0  |0  |0  |1  |0  |0  |0  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   7|1  |0  |0  |0  |1  |0  |0  |1  |F  |0  |1  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   8|1  |0  |0  |0  |1  |0  |0  |1  |F  |1  |0  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode   9|1  |0  |0  |0  |0  |1  |0  |1  |F  |1  |0  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode  10|1  |0  |0  |0  |0  |1  |0  |1  |F  |1  |1  |0  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode  11|1  |0  |0  |0  |0  |1  |0  |1  |F  |1  |1  |1  |0  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode  12|1  |0  |0  |0  |0  |1  |0  |1  |F  |1  |1  |1  |1  |0  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode  13|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |1  |0  |1  |1  |0  |1  |1  |0  |F  |
|mode  14|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |1  |0  |1  |0  |0  |0  |1  |0  |F  |
|mode  15|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |0  |1  |0  |0  |1  |0  |1  |1  |1  |0  |F  |
|mode  16|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |0  |1  |0  |0  |1  |0  |0  |0  |0  |1  |F  |
|mode  17|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |1  |0  |1  |1  |0  |0  |1  |0  |1  |F  |
|mode  18|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |1  |0  |1  |1  |0  |0  |1  |1  |0  |1  |1  |0  |F  |
|mode  19|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |0  |0  |1  |1  |0  |0  |1  |1  |0  |1  |1  |0  |F  |
|mode  20|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |S  |S  |1  |1  |1  |0  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode  21|0  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |S  |S  |1  |1  |1  |0  |0  |1  |0  |0  |1  |0  |0  |F  |
|mode  22|1  |1  |0  |0  |0  |0  |1  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |S  |S  |1  |1  |1  |0  |0  |1  |0  |0  |1  |0  |0  |F  |
|mode  23|1  |1  |1  |1  |0  |0  |0  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |S  |S  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode  24|1  |0  |0  |1  |0  |0  |0  |0  |F  |1  |1  |1  |1  |1  |1  |0  |1  |0  |S  |S  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode  25|0  |0  |0  |1  |0  |0  |0  |0  |F  |1  |1  |1  |1  |1  |1  |1  |1  |1  |S  |S  |1  |1  |1  |1  |0  |1  |0  |0  |0  |0  |0  |F  |
|mode  26|0  |0  |1  |K  |K  |K  |K  |K  |FC |K  |K  |K  |K  |1  |1  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |
|mode  27|1  |0  |1  |K  |K  |K  |K  |K  |FC |K  |K  |K  |K  |1  |1  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |
|mode  28|0  |1  |1  |K  |K  |K  |K  |K  |FC |K  |K  |K  |K  |1  |1  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |K  |

## Mode 0

VDC 150 mV

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |1   |0   |0   |0   |1   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,0|0,0,0|
|Vi/2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|1|F|
|ON|OFF|OFF|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 1

VDC 1.5 V

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |0   |1   |0   |0   |1   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,0|0,0,0|
|Vi/2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|0|0|1|F|
|OFF|ON|OFF|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 2

VDC 15 V

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |0   |0   |1   |0   |1   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,0|0,0,0|
|Vi/2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|F|
|OFF|OFF|ON|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 3

VDC 150 V

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |0   |1   |0   |0   |0   |F   |1   |1   |1   |1   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,0|0,0,0|
|Vi/2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|0|0|0|F|
|OFF|ON|OFF|OFF|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|0|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 4

VDC 1500 V

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |0   |0   |1   |0   |0   |F   |1   |1   |1   |1   |1   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,0|0,0,0|
|Vi/2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|0|F|
|OFF|OFF|ON|OFF|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|0|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|ON|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 5

IDC 15 mA

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |1   |0   |0   |0   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,0|0,0,0|
|Vi/2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|F|
|ON|OFF|OFF|OFF|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|0|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|ON|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 6

IDC 1.5 A

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |1   |0   |0   |0   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,0|0,0,0|
|Vi/2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|F|
|ON|OFF|OFF|OFF|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|0|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|ON|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 7

OHMS 150 Ω

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |1   |0   |0   |1   |F   |0   |1   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,0,0|1,0,0|
|Vi||

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|0|0|1|F|
|OFF|ON|OFF|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|1|1|0|1|1|1|1|1|1|
|ON|OFF|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 8

OHMS 1.5 kΩ

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |1   |0   |0   |1   |F   |1   |0   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,0,0|1,0,0|
|Vi||

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|0|0|1|F|
|OFF|ON|OFF|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|1|1|1|1|1|1|
|OFF|ON|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 9

OHMS 15 kΩ

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |0   |1   |0   |1   |F   |1   |0   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,0,0|1,0,0|
|Vi||

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|F|
|OFF|OFF|ON|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|1|1|1|1|1|1|
|OFF|ON|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 10

OHMS 150 kΩ

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |0   |1   |0   |1   |F   |1   |1   |0   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,0,0|1,0,0|
|Vi||

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|F|
|OFF|OFF|ON|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|0|1|0|1|1|1|1|1|1|
|OFF|OFF|ON|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 11

OHMS 1.5 MΩ

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |0   |1   |0   |1   |F   |1   |1   |1   |0   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,0,0|1,0,0|
|Vi||

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|F|
|OFF|OFF|ON|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|0|0|1|1|1|1|1|1|
|OFF|OFF|OFF|ON|ON|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 12

OHMS 15 MΩ

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |0   |0   |1   |0   |1   |F   |1   |1   |1   |1   |0   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,0,0|1,0,0|
|Vi||

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|1|0|1|F|
|OFF|OFF|ON|OFF|ON|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|0|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|ON|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 13

VAC 150 mV

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |1   |0   |1   |1   |0   |1   |1   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|1,0|1,1,0|
|I1 out|I2 out|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|0|1|0|F|
|ON|ON|OFF|ON|OFF|OFF|-|

## Mode 14

VAC 1.5 V

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |1   |0   |1   |0   |0   |0   |1   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,1,0|
|GND|I1 out|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|0|1|0|F|
|ON|ON|OFF|ON|OFF|OFF|-|

## Mode 15

VAC 15 V

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |0   |1   |0   |0   |1   |0   |1   |1   |1   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,1|1,1,0|
|I8 out|I2 out|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|1|0|0|F|
|ON|ON|ON|OFF|ON|OFF|-|

## Mode 16

VAC 150 V

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |0   |1   |0   |0   |1   |0   |0   |0   |0   |1   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,1|
|GND|I8 out|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|1|0|0|F|
|ON|ON|ON|OFF|ON|OFF|-|

## Mode 17

VAC 1500 V

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |1   |0   |1   |1   |0   |0   |1   |0   |1   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|1,0,1|
|GND|I11 out|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|1|F|
|ON|ON|OFF|OFF|ON|ON|-|

## Mode 18

IAC 15 mA

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |1   |0   |1   |1   |0   |0   |1   |1   |0   |1   |1   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|0|1|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|ON|OFF|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|1,0|1,1,0|
|I1 out|I2 out|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|0|F|
|ON|ON|OFF|OFF|ON|OFF|-|

## Mode 19

IAC 1.5 A

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |1   |0   |0   |1   |1   |0   |0   |1   |1   |0   |1   |1   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|1|0|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|OFF|ON|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|1,0|1,1,0|
|I1 out|I2 out|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|1|0|0|F|
|ON|ON|OFF|OFF|ON|OFF|-|

## Mode 20

Cal AC/DC 1

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |S   |S   |1   |1   |1   |0   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|S|S|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|0|0|F|
|ON|OFF|OFF|OFF|ON|OFF|-|

## Mode 21

Cal AC/DC 2

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |S   |S   |1   |1   |1   |0   |0   |1   |0   |0   |1   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,0|0,1,0|
|AC1|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|S|S|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|1,0,0|
|GND|-5V test|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|0|0|F|
|ON|OFF|OFF|OFF|ON|OFF|-|

## Mode 22

Cal AC/DC mer u

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |1   |0   |0   |0   |0   |1   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |S   |S   |1   |1   |1   |0   |0   |1   |0   |0   |1   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,1,0|1,1,0|
|AC2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|0|0|0|1|0|F|
|OFF|OFF|OFF|ON|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|S|S|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|1,0,0|
|GND|-5V test|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|0|0|F|
|ON|OFF|OFF|OFF|ON|OFF|-|

## Mode 23

Cal DIV zero

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |1   |1   |1   |0   |0   |0   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |S   |S   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,1,1|1,1,1|
|Vi|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|F|
|ON|OFF|OFF|OFF|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|S|S|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 24

Cal DIV cal

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |0   |1   |0   |0   |0   |0   |F   |1   |1   |1   |1   |1   |1   |0   |1   |0   |S   |S   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,0,0|1,0,0|
|Vi||

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|F|
|ON|OFF|OFF|OFF|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|0|1|0|S|S|
|OFF|OFF|OFF|OFF|OFF|ON|ON|OFF|ON|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 25

Cal I zero

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |0   |1   |0   |0   |0   |0   |F   |1   |1   |1   |1   |1   |1   |1   |1   |1   |S   |S   |1   |1   |1   |1   |0   |1   |0   |0   |0   |0   |0   |F   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,0|0,0,0|
|Vi/2|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|0|0|0|F|
|ON|OFF|OFF|OFF|OFF|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|1|S|S|
|OFF|OFF|OFF|OFF|OFF|ON|OFF|OFF|OFF|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|0,0|0,0,0|
|GND|GND|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|0|F|
|ON|OFF|OFF|OFF|OFF|OFF|-|

## Mode 26

Cal ADC GND

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |0   |1   |K   |K   |K   |K   |K   |FC  |K   |K   |K   |K   |1   |1   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,0,1|0,0,1|
|GND|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|K|FC|
|-|-|-|-|-|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|1|1|K|K|K|K|K|
|-|-|-|-|OFF|ON|-|-|-|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|K,K|K,K,K|
|-|-|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|K|K|K|K|K|K|
|ON|-|-|-|-|-|-|

## Mode 27

Cal ADC CAL+

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|1   |0   |1   |K   |K   |K   |K   |K   |FC  |K   |K   |K   |K   |1   |1   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|1,0,1|1,0,1|
|CAL+|CAL-|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|K|FC|
|-|-|-|-|-|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|1|1|K|K|K|K|K|
|-|-|-|-|OFF|ON|-|-|-|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|K,K|K,K,K|
|-|-|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|K|K|K|K|K|K|
|ON|-|-|-|-|-|-|

## Mode 28

Cal ADC CAL-

**Signal values**

|A0  |A1  |A2  |S1  |S2  |S3  |S4  |S5  |S6  |S7  |S8  |S9  |S10 |S11 |S12 |S13 |S14 |S15 |S16 |S17 |S18 |S19 |S20 |S21 |S22 |S23 |S24 |S25 |S26 |S27 |S28 |S29 |
|:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |
|0   |1   |1   |K   |K   |K   |K   |K   |FC  |K   |K   |K   |K   |1   |1   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |K   |

**D1639 multiplexers**

|I5<br/>(A0, A1, A2)<br/>*ADC+ input mux*|I4<br/>(A0, A1, A2)<br/>*CAL+/- grounding mux*|
|:-:|:-:|
|0,1,1|0,1,1|
|CAL-|CAL+|

**D1639 switches**

|T3<br/>(S1)|T4<br/>(S2)|T5<br/>(S3)|T6<br/>(S4)|Re1<br/>(S5)|Re2<br/>(S6)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|K|FC|
|-|-|-|-|-|-|

**D1640 switches**

|Re1,2<br/>(S7)<br/>*inv*|Re3<br/>(S8)<br/>*inv*|Re4<br/>(S9)<br/>*inv*|Re5<br/>(S10)<br/>*inv*|Re6~9<br/>(S11)<br/>*inv*|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~14*|Re10<br/>(S13)<br/>*inv*|Re11<br/>(S14)<br/>*inv*|Re12<br/>(S15)<br/>*inv*|Re13<br/>(S16)<br/>*inv*|Re14<br/>(S17)<br/>*inv*|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|K|K|K|K|1|1|K|K|K|K|K|
|-|-|-|-|OFF|ON|-|-|-|-|-|

**D1638 multiplexers**

|I4<br/>(S24, S25)<br/>*I2 (x10 amp) input mux*|I5<br/>(S26, S27, S28)<br/>*I9 (RMS converter) input mux*|
|:-:|:-:|
|K,K|K,K,K|
|-|-|

**D1638 switches**

|+5V RELAY EN<br/>(S12)<br/>*Unblocks Re1~4*|Re1<br/>(S18)<br/>*inv*|Re2<br/>(S19)<br/>*inv*|Re3<br/>(S20)<br/>*inv*|Re4<br/>(S21)<br/>*inv*|Re5<br/>(S22)|T8, I7<br/>(S29)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|K|K|K|K|K|K|
|ON|-|-|-|-|-|-|

