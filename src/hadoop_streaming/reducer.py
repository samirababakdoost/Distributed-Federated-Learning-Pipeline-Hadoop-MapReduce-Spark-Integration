#!/usr/bin/env python3
import sys
current_client = None
sum_val = 0.0
count = 0
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    client_id, val_str = line.split('\t')
    feature_val, one = val_str.split(',')
    if current_client == client_id:
        sum_val += float(feature_val)
        count += int(one)
    else:
        if current_client:
            print(f"{current_client},{sum_val},{count}")
        current_client = client_id
        sum_val = float(feature_val)
        count = int(one)
if current_client:
    print(f"{current_client},{sum_val},{count}")
