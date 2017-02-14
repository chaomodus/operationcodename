# -*- python -*-

import bobo
import json
import fnmatch
import os
import os.path
import syslog
import sys
import jinja2
import webob
import mimetypes

try:
	config = json.load(file('/srv/operationcodename/operationcodename.cfg','r'))
except:
	config = dict()
try:
        sys.path.append(os.path.dirname(__file__))
except: pass

import namegenerators


@bobo.resource('/', content_type="text/html")
def index(request): return file('operationcodename.template','r').read()

@bobo.query('/namegen',content_type="application/json")
def namegen(bobo_request, seed='1.0'):
        namegenerators.filters.filter_random.seed(seed)
        namegenerators.codename.codename_random.seed(seed)
	name = namegenerators.codename.code_name()
	return json.dumps({'seed':seed, 'codename':name})


@bobo.resource('/statics/:f')
@bobo.resource('/resources/:f')
def statics(bobo_request, f):
	f = f.replace('..','fuuuuuuuuuuuuuuuuuuuug')
	f = f.replace('/','asssssssssssssssssssss')
	pth = os.path.join('resources',f)
	response = webob.Response()
        content_type = mimetypes.guess_type(pth)[0]
        if content_type is not None:
		response.content_type = content_type
        try:
		response.body = file(pth,'r').read()
        except IOError:
		raise bobo.NotFound
	return response



if not __name__ == 'bobo__main__':
	application = bobo.Application(bobo_resources=__name__)
