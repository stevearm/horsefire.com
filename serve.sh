#!/bin/bash
cd $(dirname $0)
pelican
cd output
python -m SimpleHTTPServer
