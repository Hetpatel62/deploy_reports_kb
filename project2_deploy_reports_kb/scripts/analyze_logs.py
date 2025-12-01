#!/usr/bin/env python3
import os, json, re
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
def analyze():
    summary = {'total':0, 'by_level':{}}
    for fname in os.listdir(LOG_DIR):
        if not fname.endswith('.log'): continue
        with open(os.path.join(LOG_DIR,fname)) as f:
            for line in f:
                summary['total'] += 1
                m = re.match(r'\[(\w+)\]', line)
                level = m.group(1) if m else 'UNKNOWN'
                summary['by_level'][level] = summary['by_level'].get(level,0)+1
    print('Log summary:')
    print(json.dumps(summary, indent=2))
if __name__ == '__main__':
    analyze()
