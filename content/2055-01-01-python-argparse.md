Title: Failing to concat HDFS files
Tags: hadoop, documentation
Date: 2015-02-15T00:32

Python 2.7's argparse does not work correctly with subparsers. If you define `--verbose` on the top level, and have a subparser for `run`, then running `script.py run --verbose` will fail. http://bugs.python.org/issue9253
