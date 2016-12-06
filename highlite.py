#! /usr/bin/env python3

import re
import sys


highlite_color = "\033[93m"
normal_color = "\033[39m"


def syntax():
    print("Invalid syntax")


def scan(buf, target):
    for line in buf:
        res = [(a.start(), a.end()) for a in list(re.finditer(target, line))]
        if res is not None:
            offset = 0
            for x in res:
                start = x[0] + offset
                end = x[1] + offset
                line = line[:start] + highlite_color + line[start:end] + normal_color + line[end:]
                offset += 10
        print(line)


def main():
    if len(sys.argv) == 2:
        if not sys.stdin.isatty():
            text = sys.stdin.read()
            scan(text.split("\n"), sys.argv[1])
        else:
            syntax()
    elif len(sys.argv) == 3:
        f = open(sys.argv[2], 'r')
        text = f.read()
        scan(text.split("\n"), sys.argv[1])
        f.close()
    elif len(sys.argv) == 0:
        syntax()

if __name__ == "__main__":
        main()
