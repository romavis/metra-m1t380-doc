#!/usr/bin/env python3

import os
import struct
from abc import abstractmethod
from typing import Mapping, Sequence, Union


REPO = os.path.normpath(os.path.dirname(__file__) + '/..')
FW = REPO + '/files/fw/8748/M1T380_i8748/MHB8748.bin'

SIG_NAMES = tuple(f'A{i}' for i in range(3)) + tuple(f'S{i}' for i in range(1, 30))


class SigInterpreter:
    @abstractmethod
    def value(self, val: Union[int, str]) -> str:
        ...


class Switch(SigInterpreter):
    def __init__(self, inv: bool):
        self.inv = inv

    def value(self, val: Union[int, str]) -> str:
        if isinstance(val, str):
                return val
        else:
            if bool(val) ^ bool(self.inv):
                return 'ON'
            else:
                return 'OFF'


class Multiplexer(SigInterpreter):
    def __init__(self, values: Mapping[int, str]):
        self.values = values

    def value(self, val: Union[int, str]) -> str:
        if isinstance(val, str):
            return val
        elif val in self.values:
            return self.values[val]
        else:
            return '??'


class SigConsumer:
    def __init__(self, board: str, device: str, bits: Sequence[str], interp: SigInterpreter, desc: str = ''):
        self.board = board
        self.device = device
        self.bits = bits
        self.bit_idxs = [SIG_NAMES.index(b) for b in bits]
        self.interp = interp
        self.desc = desc

    def value(self, sig: Mapping[str, Union[int, str]]) -> str:
        return ','.join(str(sig[b]) for b in self.bits)

    def state(self, sig: Mapping[str, Union[int, str]]) -> str:
        vi = 0
        for i, n in enumerate(self.bits):
            v = sig[n]
            if isinstance(v, int):
                assert v in (0, 1)
                vi |= v << i
            else:
                return ''
        return self.interp.value(vi)


SIG_USERS = (
    #
    # D1639
    #
    SigConsumer('D1639', 'I5', ['A0', 'A1', 'A2'], Multiplexer(
        {
            0: 'k * Vin / 2',
            1: 'k * Vin',
            2: 'AC1 (ADC measures AC/DC converter RMS out)',
            3: 'AC2 (ADC measures AC/DC converter\'s -5V ref voltage)',
            4: 'GND',
            5: 'CAL+',
            6: 'CAL-',
            7: 'k * Vin'
        }
    ), desc='selects signal that goes to ADC input'),
    SigConsumer('D1639', 'I4', ['A0', 'A1', 'A2'], Multiplexer(
        {
            0: 'CAL-',
            1: 'none',
            2: 'CAL-',
            3: 'CAL-',
            4: 'CAL-',
            5: 'CAL-',
            6: 'CAL+',
            7: 'CAL-'
        }
    ), desc='grounds selected signal on ADC board'),
    SigConsumer('D1639', 'T3', ['S1'], Switch(False)),
    SigConsumer('D1639', 'T4', ['S2'], Switch(False)),
    SigConsumer('D1639', 'T5', ['S3'], Switch(False)),
    SigConsumer('D1639', 'T6', ['S4'], Switch(False)),
    SigConsumer('D1639', 'T3~6', ['S1', 'S2', 'S3', 'S4'], Multiplexer({
        1: 'input amp k=-100 (T3 on)',
        2: 'input amp k=-10 (T4 on)',
        4: 'input amp k=-1 (T5 on)',
        8: 'input amp off (T6 on)',
    }), desc='controls input amplifier gain'),
    SigConsumer('D1639', 'Re1', ['S5'], Switch(False)),
    SigConsumer('D1639', 'Re2', ['S6'], Switch(False)),
    SigConsumer('D1639', 'Re1', ['S5'], Multiplexer({
        0: 'Vin comes from H1 (from input voltage divider or current shunt)',
        1: 'Vin comes directly from H terminal',
    }), desc='takes Vin either from H or from H1 terminal'),
    #
    # D1642
    #
    SigConsumer('D1642', 'Re1,2', ['S7'], Switch(True)),
    SigConsumer('D1642', 'Re3', ['S8'], Switch(True)),
    SigConsumer('D1642', 'Re4', ['S9'], Switch(True)),
    SigConsumer('D1642', 'Re5', ['S10'], Switch(True)),
    SigConsumer('D1642', 'Re6~9', ['S11'], Switch(True)),
    SigConsumer('D1642', '+5V RELAY EN', ['S12'], Switch(False),
                desc='Unblocks Re1~14'),
    SigConsumer('D1642', 'Re10', ['S13'], Switch(True)),
    SigConsumer('D1642', 'Re11', ['S14'], Switch(True)),
    SigConsumer('D1642', 'Re12', ['S15'], Switch(True)),
    SigConsumer('D1642', 'Re13', ['S16'], Switch(True)),
    SigConsumer('D1642', 'Re14', ['S17'], Switch(True)),
    SigConsumer('D1642', 'Re10~12', ['S13','S14','S15'], Multiplexer(
        {
            0b111: 'input voltage divider disconnected',
            0b010: 'input voltage divider connected to CAL+:CAL- source',
            0b101: 'input voltage divider connected to H1KV terminal',
            0b110: 'input voltage divider connected to H terminal',
        }
    ), desc='connects and disconnects sources to input divider'),
    SigConsumer('D1642', 'Re13,14', ['S16', 'S17'], Multiplexer(
        {
            0b11: 'H:L are not connected to current shunts',
            0b10: 'H:L are connected to 10 Ω shunt',
            0b01: 'H:L are connected to 0.1 Ω shunt',
            0b00: 'H:L are shorted through diodes, but not connected to current shunts',
        }
    ), desc='connects and disconnects current shunt resistors'),
    SigConsumer('D1642', 'Re6~9', ['S11'], Multiplexer(
        {
            1: 'current source disconnected',
            0: 'current source connected, Hx:Lx or H:L selected via OHMS 2-4 switch'
        }
    ), desc='connects current source to Hx:Lx or H:L terminals'),
    SigConsumer('D1642', 'Re1~5', ['S7', 'S8', 'S9', 'S10'], Multiplexer(
        {
            0b1111: 'Imeas = 0.5 uA (Re1~5 off)',
            0b0111: 'Imeas = 5 uA (Re5 on)',
            0b1011: 'Imeas = 50 uA (Re4 on)',
            0b1101: 'Imeas = 0.5 mA (Re3 on)',
            0b1110: 'Imeas = 5 mA (Re1,2 on)',
        }
    ), desc='controls Hx-Lx current source for OHMS measurement'),
    #
    # D1638
    #
    SigConsumer('D1638', '+5V RELAY EN', ['S12'], Switch(False),
                desc='Unblocks Re1~4'),
    SigConsumer('D1638', 'Re1', ['S18'], Switch(True)),
    SigConsumer('D1638', 'Re2', ['S19'], Switch(True)),
    SigConsumer('D1638', 'Re3', ['S20'], Switch(True)),
    SigConsumer('D1638', 'Re4', ['S21'], Switch(True)),
    SigConsumer('D1638', 'Re5', ['S22'], Switch(False)),
    SigConsumer('D1638', 'T8, I7', ['S29'], Switch(False)),
    SigConsumer('D1638', 'Re1~5', ['S18', 'S19', 'S20', 'S21', 'S22'], Multiplexer(
        {
            0b01111: 'AC/DC converter disconnected from all input terminals',
            0b01100: 'H -> I8; L -> GND',
            0b00100: 'H -> I8;  F1 -> I1; L -> GND',
            0b01010: 'H -> I1; L -> GND',
            0b00110: 'F1 -> I1; L -> GND',
            0b10110: 'H1KV -> I11;  F1 -> I1; L -> GND',
            0b00111: 'F1 -> I1;  but L is disconnected!',
        }
    ), desc='connects and disconnects AC/DC converter inputs'),
    SigConsumer('D1638', 'I4', ['S24', 'S25'], Multiplexer(
        {
            0: 'GND',
            1: 'I1 out (H/F1 voltage x3.0)',
            2: 'I8 out (H voltage x0.03)',
            3: 'GND'
        }
    ), desc='selects input to I2 (x10 amplifier)'),
    SigConsumer('D1638', 'I5', ['S26', 'S27', 'S28'], Multiplexer(
        {
            0: 'GND',
            1: '-5V ref',
            2: 'I1 out (H/F1 voltage x3.0)',
            3: 'I2 out (see I2 input routing above)',
            4: 'I8 out (H voltage x0.03)',
            5: 'I11 out (H1KV voltage x0.003)',
            6: 'GND',
            7: 'GND'
        }
    ), desc='selects input to I9 (RMS converter)'),
)


# Set switch descriptions to 'inv' if those switches are inverted
for c in SIG_USERS:
    if not c.desc and isinstance(c.interp, Switch):
        if c.interp.inv:
            c.desc = 'inv'


class Mode:
    def __init__(self, idx: int, mreg: int):
        self.mreg = mreg
        self.idx = idx
        self.sig = {}
        self.shortdesc = ''
        self.desc = []
        for i in range(len(SIG_NAMES)):
            bit = (mreg >> i) & 1
            self.sig[SIG_NAMES[i]] = bit

    def describe(self) -> Sequence[str]:
        l = []
        l.append(f'## Mode {self.idx}')
        l.append('')
        l.append(self.shortdesc)
        l.append('')
        if self.desc:
            l.extend(self.desc)
            l.append('')
        l.append('**MREG signal values**')
        l.append('')
        l.append('|' + '|'.join(f'{n:4s}' for n in SIG_NAMES) + '|')
        l.append('|' + '|'.join(':-: ' for _ in SIG_NAMES) + '|')
        l.append('|' + '|'.join(f'{str(b):4s}' for b in self.sig.values()) + '|')
        l.append('')
        boards = dict.fromkeys(c.board for c in SIG_USERS)

        def ptable(cons: Sequence[SigConsumer]) -> Sequence[str]:
            b = []
            mh = []
            for c in cons:
                sigs = ', '.join(c.bits)
                s = f'{c.device}<br/>({sigs})'
                if c.desc:
                    s += f'<br/>*{c.desc}*'
                mh.append(s)
            b.append('|' + '|'.join(mh) + '|')
            b.append('|' + '|'.join(':-:' for _ in cons) + '|')
            b.append('|' + '|'.join(f'{c.value(self.sig)}' for c in cons) + '|')
            b.append('|' + '|'.join(f'{c.state(self.sig)}' for c in cons) + '|')
            return b

        for b in boards:
            swchs = [c for c in SIG_USERS if c.board == b and isinstance(c.interp, Switch)]
            l.append(f'**Board {b} switches**')
            l.append('')
            l.extend(ptable(swchs))
            l.append('')

        muxes = [c for c in SIG_USERS if isinstance(c.interp, Multiplexer)]
        if muxes:
            l.append('**State decoding**')
            l.append('')
            l.append('```')
            for m in muxes:
                bs = ','.join(m.bits)
                l.append(f'{m.board} - {m.device} - {m.desc}')
                st = m.state(self.sig)
                if st:
                    l.append(f'    SELECTED: {st}')
                l.append(f'    [({bs}) = ({m.value(self.sig)})]')
                l.append('')
            l.append('```')
            l.append('')
        return l


with open(FW, 'rb') as f:
    fw_bytes = f.read()

tbl_mreg = fw_bytes[0x368:0x3d0]
assert len(tbl_mreg) == 4 * 26

modes = {}

# Add modes from ROM
for i in range(26):
    mreg = struct.unpack('<I', tbl_mreg[4*i:4*(i+1)])[0]
    mode = Mode(i, mreg)
    # FILTER control
    mode.sig['S6'] = 'fil'
    mode.sig['S29'] = 'fil'
    # Re13/14 logic for calibration in IAC/VAC modes
    if i >= 20:
        mode.sig['S16'] = 'CS'
        mode.sig['S17'] = 'CS'
    modes[i] = mode


# Add calibration modes
for i in range(26, 29):
    # Use mode 0 as a starting point
    mode = Mode(i, modes[0].mreg)
    # Patch
    a02patches = {
        26: {'A2': 1, 'A1': 0, 'A0': 0},
        27: {'A2': 1, 'A1': 0, 'A0': 1},
        28: {'A2': 1, 'A1': 1, 'A0': 0}
    }
    mode.sig.update(a02patches[i])
    # All Sx signals keep their state
    for s in mode.sig:
        if s.startswith('S'):
            mode.sig[s] = 'K'
    # Disable Re6~9, enable +5V RELAY EN
    mode.sig['S11'] = 1
    mode.sig['S12'] = 1
    # Re2 (D1639) needs special handling
    mode.sig['S6'] = 'CF'
    modes[i] = mode


# Annotate modes
MODE_SHORTDESC = {
    0: 'VDC 150 mV',
    1: 'VDC 1.5 V',
    2: 'VDC 15 V',
    3: 'VDC 150 V',
    4: 'VDC 1500 V',
    5: 'IDC 15 mA',
    6: 'IDC 1.5 A',
    7: 'OHMS 150 Ω',
    8: 'OHMS 1.5 kΩ',
    9: 'OHMS 15 kΩ',
    10: 'OHMS 150 kΩ',
    11: 'OHMS 1.5 MΩ',
    12: 'OHMS 15 MΩ',
    13: 'VAC 150 mV',
    14: 'VAC 1.5 V',
    15: 'VAC 15 V',
    16: 'VAC 150 V',
    17: 'VAC 1500 V',
    18: 'IAC 15 mA',
    19: 'IAC 1.5 A',
    20: 'Cal AC/DC zero',
    21: 'Cal AC/DC -5Vref',
    22: 'Cal meas -5Vref',
    23: 'Cal DIV zero',
    24: 'Cal DIV CAL+',
    25: 'Cal DIV Izero',
    26: 'Cal ADC zero',
    27: 'Cal ADC CAL+',
    28: 'Cal ADC CAL-'
}


for i in MODE_SHORTDESC:
    modes[i].shortdesc = MODE_SHORTDESC[i]


def signal_overview():
    l = []
    l.append('## Overview table')
    l.append('')
    l.append('|        |' + '|'.join(f'{s:3s}' for s in SIG_NAMES) + '|')
    l.append('| :-:    |' + '|'.join(':-:' for _ in SIG_NAMES) + '|')
    for i in modes:
        sig = modes[i].sig
        l.append(f'|mode{i:<3d}|' + '|'.join(f'{sig[s]!s:3s}' for s in SIG_NAMES) + '|')
    l.append('')
    return l


#
# Print header, followed by TOC,
# Then signal overview table, followed by descriptive per-mode tables
#
hdr = [
    '# Modes',
    ''
]
for i in modes:
    hdr.append(f'- [Mode {i}](#mode-{i}): {modes[i].shortdesc}')
hdr.append('')
hdr.extend([
    '**NOTE** - in this document we use following symbols to mark special or variable states:',
    ' - **fil** - MREG bit is equal to `fil` parameter of *set_mode* command.',
    ' - **K** - MREG bit value is unchanged by *set_mode* - so it keeps its value that it had before '
    '*set_mode* command was executed.',
    ' - **CF** - if current source was enabled prior to entering this mode (Re6~9 @ D1642 were on), '
    'Re2 @ D1639 will be switched off; otherwise behaves like `fil`.',
    ' - **CS** - if one of Re13,14 was enabled prior to entering this mode, both Re13,14 will be turned on, '
    'disconnecting input terminals H:L from the current shunts and shorting them through diodes D5,D6.',
    ''
])

print('\n'.join(hdr))
print('\n'.join(signal_overview()))
for m in modes.values():
    print('\n'.join(m.describe()))
