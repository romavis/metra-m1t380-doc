#!/usr/bin/env python3

import os
import struct
from abc import abstractmethod
from typing import Mapping, Sequence, Union


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
            if self.inv:
                return '~' + val
            else:
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
        else:
            return self.values[val]


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
                return '-'
        return self.interp.value(vi)


SIG_USERS = (
    # D1639 mux
    SigConsumer('D1639', 'I5', ['A0', 'A1', 'A2'], Multiplexer(
        {
            0: 'Vi/2',
            1: 'Vi',
            2: 'AC1',
            3: 'AC2',
            4: 'GND',
            5: 'CAL+',
            6: 'CAL-',
            7: 'Vi'
        }
    ), desc='ADC+ input mux'),
    SigConsumer('D1639', 'I4', ['A0', 'A1', 'A2'], Multiplexer(
        {
            0: 'CAL-',
            1: '',
            2: 'CAL-',
            3: 'CAL-',
            4: 'CAL-',
            5: 'CAL-',
            6: 'CAL+',
            7: 'CAL-'
        }
    ), desc='CAL+/- grounding mux'),
    # D1639 switches
    SigConsumer('D1639', 'T3', ['S1'], Switch(False)),
    SigConsumer('D1639', 'T4', ['S2'], Switch(False)),
    SigConsumer('D1639', 'T5', ['S3'], Switch(False)),
    SigConsumer('D1639', 'T6', ['S4'], Switch(False)),
    SigConsumer('D1639', 'Re1', ['S5'], Switch(False)),
    SigConsumer('D1639', 'Re2', ['S6'], Switch(False)),
    # D1642 switches
    SigConsumer('D1640', 'Re1,2', ['S7'], Switch(True)),
    SigConsumer('D1640', 'Re3', ['S8'], Switch(True)),
    SigConsumer('D1640', 'Re4', ['S9'], Switch(True)),
    SigConsumer('D1640', 'Re5', ['S10'], Switch(True)),
    SigConsumer('D1640', 'Re6~9', ['S11'], Switch(True)),
    SigConsumer('D1640', '+5V RELAY EN', ['S12'], Switch(False),
                desc='Unblocks Re1~14'),
    SigConsumer('D1640', 'Re10', ['S13'], Switch(True)),
    SigConsumer('D1640', 'Re11', ['S14'], Switch(True)),
    SigConsumer('D1640', 'Re12', ['S15'], Switch(True)),
    SigConsumer('D1640', 'Re13', ['S16'], Switch(True)),
    SigConsumer('D1640', 'Re14', ['S17'], Switch(True)),
    # D1638 muxes
    SigConsumer('D1638', 'I4', ['S24', 'S25'], Multiplexer(
        {
            0: 'GND',
            1: 'I1 out',
            2: 'I8 out',
            3: 'GND'
        }
    ), desc='I2 (x10 amp) input mux'),
    SigConsumer('D1638', 'I5', ['S26', 'S27', 'S28'], Multiplexer(
        {
            0: 'GND',
            1: '-5V test',
            2: 'I1 out',
            3: 'I2 out',
            4: 'I8 out',
            5: 'I11 out',
            6: 'GND',
            7: 'GND'
        }
    ), desc='I9 (RMS converter) input mux'),
    # D1638 switches
    SigConsumer('D1638', '+5V RELAY EN', ['S12'], Switch(False),
                desc='Unblocks Re1~4'),
    SigConsumer('D1638', 'Re1', ['S18'], Switch(True)),
    SigConsumer('D1638', 'Re2', ['S19'], Switch(True)),
    SigConsumer('D1638', 'Re3', ['S20'], Switch(True)),
    SigConsumer('D1638', 'Re4', ['S21'], Switch(True)),
    SigConsumer('D1638', 'Re5', ['S22'], Switch(False)),
    SigConsumer('D1638', 'T8, I7', ['S29'], Switch(False)),
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
        l.append('**Signal values**')
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
            muxes = [c for c in SIG_USERS if c.board == b and isinstance(c.interp, Multiplexer)]
            swchs = [c for c in SIG_USERS if c.board == b and isinstance(c.interp, Switch)]
            if muxes:
                l.append(f'**{b} multiplexers**')
                l.append('')
                l.extend(ptable(muxes))
                l.append('')
            if swchs:
                l.append(f'**{b} switches**')
                l.append('')
                l.extend(ptable(swchs))
                l.append('')
        return l


REPO = os.path.normpath(os.path.dirname(__file__) + '/../..')
FW = REPO + '/fw/8748/M1T380_i8748/MHB8748.bin'


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
    mode.sig['S6'] = 'F'
    mode.sig['S29'] = 'F'
    # Re13/14 logic for calibration in IAC/VAC modes
    if i >= 20:
        mode.sig['S16'] = 'S'
        mode.sig['S17'] = 'S'
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
    mode.sig['S6'] = 'FC'
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
    20: 'Cal AC/DC 1',
    21: 'Cal AC/DC 2',
    22: 'Cal AC/DC mer u',
    23: 'Cal DIV zero',
    24: 'Cal DIV cal',
    25: 'Cal I zero',
    26: 'Cal ADC GND',
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
        l.append(f'|mode {i:3d}|' + '|'.join(f'{sig[s]!s:3s}' for s in SIG_NAMES) + '|')
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

print('\n'.join(hdr))
print('\n'.join(signal_overview()))
for m in modes.values():
    print('\n'.join(m.describe()))
