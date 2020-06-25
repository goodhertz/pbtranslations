from runpy import run_path
from pathlib import Path
import argparse, importlib, inspect, json, ast
from pprint import pprint

parser = argparse.ArgumentParser(prog="PBT", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("catalog", type=str)
args = parser.parse_args()

catalog = "{:04d}".format(int(args.catalog))
path = Path(f"plugins/{catalog}.py")

program = run_path(str(path))

ts = program["ts"]

for t in ts:
    if t.warnings:
        print("---")
        pprint(t)
        print(">>>>>>>>", t.warnings)