#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('client_id'):
        continue
    parts = line.split(',')
    if len(parts) >= 2:
        print(f"{parts[0]}\t{parts[1]},1")
