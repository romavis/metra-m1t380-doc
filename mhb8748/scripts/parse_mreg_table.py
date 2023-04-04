#!/usr/bin/env python3

import os
import struct

REPO = os.path.normpath(os.path.dirname(__file__) + '/../..')
FW = REPO + '/fw/8748/M1T380_i8748/MHB8748.bin'


with open(FW, 'rb') as f:
    fw_bytes = f.read()

tbl_mreg = fw_bytes[0x368:0x3d0]
assert len(tbl_mreg) == 4 * 26

sig_names = []
sig_names.extend(['A0', 'A1', 'A2'])
for s in range(1,30):
    sig_names.append(f'S{s}')

sw_names = []
sw_names.extend(
    [
        ('D1639', 'A0', None),
        ('D1639', 'A1', None),
        ('D1639', 'A2', None),
        ('D1639', 'T3', 1),
        ('D1639', 'T4', 1),
        ('D1639', 'T5', 1),
        ('D1639', 'T6', 1),
        ('D1639', 'Re1', 1),
        ('D1639', 'Re2', 1),
        #
        ('D1642', 'Re1,2', 0),
        ('D1642', 'Re3', 0),
        ('D1642', 'Re4', 0),
        ('D1642', 'Re5', 0),
        ('D1642', 'Re6~9', 0),
        ('D1642', '+5V EN', 1),
        ('D1642', 'Re10', 0),
        ('D1642', 'Re11', 0),
        ('D1642', 'Re12', 0),
        ('D1642', 'Re13', 0),
        ('D1642', 'Re14', 0),
        #
        ('D1638', 'Re1', 0),
        ('D1638', 'Re2', 0),
        ('D1638', 'Re3', 0),
        ('D1638', 'Re4', 0),
        ('D1638', 'Re5', 1),
        ('D1638', 'n/a', None),
        ('D1638', 'I4 - A0', None),
        ('D1638', 'I4 - A1', None),
        ('D1638', 'I5 - A0', None),
        ('D1638', 'I5 - A1', None),
        ('D1638', 'I5 - A2', None),
        ('D1638', 'T8, I7', 1),
    ]
)

ctl_type = {
    None: '',
    0: 'inv',
    1: ''
}


# Table lists what I4,I5 connect to ground and to Sx input
# for different addresses. First entry is for I4 (connected
# to GND), second entry is for I5 (connected to Sx)
i4i5_adr_tbl = {
    0: ('CAL-', 'Vi/2'),
    1: ('',     'Vi'),
    2: ('CAL-', 'AC1'),
    3: ('CAL-', 'AC2'),
    4: ('CAL-', 'GND'),
    5: ('CAL-', 'CAL+'),
    6: ('CAL+', 'CAL-'),
    7: ('CAL-', 'Vi'),
}


def print_sig_values():
    print('MODE    |' + '|'.join(f'{n:8s}' for n in sig_names))
    for mode in range(26):
        q = struct.unpack('<I', tbl_mreg[4*mode:4*(mode+1)])[0]
        cols = []
        for i in range(32):
            b = (q >> i) & 1
            cols.append(f' {b:<7d}')
        print(f'{mode:<8d}|' + '|'.join(cols))


def print_sw_states():
    print('MODE    |' + '|'.join(f'{n:8s}' for n in sig_names))
    print('        |' + '|'.join(f'{r[0]:8s}' for r in sw_names))
    print('        |' + '|'.join(f'{r[1]:8s}' for r in sw_names))
    print('        |' + '|'.join(f'{ctl_type[r[2]]:8s}' for r in sw_names))

    for mode in range(26):
        q = struct.unpack('<I', tbl_mreg[4*mode:4*(mode+1)])[0]
        cols = []
        i4i5_adr = q & 0x7
        i4i5_sel = i4i5_adr_tbl[i4i5_adr]
        cols.append(f'0b{i4i5_adr:<03b}   ')
        cols.extend(f'{v:<8s}' for v in i4i5_sel)
        for i in range(3,32):
            b = (q >> i) & 1
            state = ''
            ctl = sw_names[i][2]
            if ctl is None:
                v = f'{b}'
            else:
                state = 'ON' if b ^ int(not bool(ctl)) else 'OFF'
                v = f'{b}: {state:3}'
                # v = f'{state:3}'
            cols.append(f' {v:<7}')
        print(f'{mode:<8d}|' + '|'.join(cols))


print_sig_values()
print('')
print('')
print_sw_states()
