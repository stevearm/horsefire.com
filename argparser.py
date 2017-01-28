#!/usr/bin/python
import argparse

# Try parent parsers: http://stackoverflow.com/questions/7498595/python-argparse-add-argument-to-multiple-subparsers

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
parser.add_argument("--verbose", action="store_true")

task = subparsers.add_parser("check")
# task.add_argument("--detailed", action="store_true")

task = subparsers.add_parser("run")
# task.add_argument("--quick", action="store_true")

args = parser.parse_args()

print args
print "Verbose is {}".format(args.verbose)
print "Detailed is {}".format(args.detailed if "detailed" in args else None)
print "Quick is {}".format(args.quick if "quick" in args else None)
