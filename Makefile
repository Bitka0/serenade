# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

all: run
init: cleardb collectstatic syncdb
run: compilemessages
	cd homepage && python2 manage.py runserver 0.0.0.0:8081
syncdb:
	cd homepage && python2 manage.py syncdb
collectstatic:
	cd homepage && python2 manage.py collectstatic --noinput
cleardb:
	- cd homepage && rm database.db
messages:
	- cd homepage && mkdir locale
	cd homepage && python2 manage.py makemessages -l de
compilemessages:
	- cd homepage && python2 manage.py compilemessages
