# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

all: run
init: cleardb collectstatic syncdb

run:
	cd homepage && python2 manage.py runserver 0.0.0.0:8081
collectstatic:
	cd homepage && python2 manage.py collectstatic --noinput
syncdb:
	cd homepage && python2 manage.py syncdb
cleardb:
	- cd homepage && rm database.db
