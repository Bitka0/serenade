all: run
run:
	cd homepage && python2 manage.py runserver 0.0.0.0:8081
