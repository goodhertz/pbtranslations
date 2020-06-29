#!/usr/bin/env python

import os
from runpy import run_path
from pathlib import Path
import argparse, importlib, inspect, json, ast
from pprint import pprint

parser = argparse.ArgumentParser(prog="PBT", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--file", type=str)
args = parser.parse_args()

#path = Path(f"plugins/{catalog}.py")
#program = run_path(str(path))

if args.file:
    resolved = Path(args.file).resolve()
    if resolved.is_dir():
        files = resolved.glob("**/*.py")
    else:
        files = [resolved]
else:
    files = (Path(__file__).parent.resolve() / "translatables").glob("**/*.py")

for py in files:
    print("\n\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n")
    print(">>>", py)
    program = run_path(str(py))
    ts = program["ts"]

    for k, t in ts.strings.items():
        if t.warnings:
            print("---")
            pprint(t)
            print(">>>>>>>>", t.warnings)