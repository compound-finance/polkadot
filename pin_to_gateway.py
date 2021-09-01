#!/usr/bin/env python

import os
from os.path import join, getsize

map = {
    'git = "https://github.com/paritytech/substrate"': 'git = "https://github.com/compound-finance/substrate"',
    'git = "https://github.com/paritytech/grandpa-bridge-gadget"': 'git = "https://github.com/compound-finance/grandpa-bridge-gadget"',
    'git = "https://github.com/paritytech/substrate.git"': 'git = "https://github.com/compound-finance/substrate"',
    'git = "https://github.com/paritytech/grandpa-bridge-gadget.git"': 'git = "https://github.com/compound-finance/grandpa-bridge-gadget"',
    'branch = "master"': 'branch = "gateway"'
}

def process_file(file_path):
    print('processing', file_path)
    with open(file_path, 'r') as infile:
        text = infile.read()
        for old, new in map.items():
            text = text.replace(old, new)
    with open(file_path, 'w') as outfile:
        outfile.write(text)

def main():
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name == 'Cargo.toml':
                process_file(join(root,name))
        if '.git' in dirs:
            dirs.remove('.git')
        if 'doc' in dirs:
            dirs.remove('doc')
        if 'docker' in dirs:
            dirs.remove('docker')

if __name__ == '__main__':
    main()