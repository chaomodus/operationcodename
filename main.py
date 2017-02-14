#!/usr/bin/python
import boboserver
import sys

args = ['-f','operationcodename.wsgi', '-p','8081']
try:
    args.extend(sys.argv[1:])
except: pass

sys.exit(boboserver.server(args=args))
