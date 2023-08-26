# Microservices Project Make File
# author: umer mansoor

VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) venv

install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch: venv shutdown
	. venv/bin/activate; python  service/movie.py &
	. venv/bin/activate; python  service/showtime.py &
	. venv/bin/activate; python  service/booking.py &
	. venv/bin/activate; python  service/user.py &

shutdown:
	ps -ef | grep "service/movie.py" | grep -v grep | awk '{print $$2}' | xargs kill  
	ps -ef | grep "service/showtime.py" | grep -v grep | awk '{print $$2}' | xargs kill  
	ps -ef | grep "service/booking.py" | grep -v grep | awk '{print $$2}' | xargs kill  
	ps -ef | grep "service/user.py" | grep -v grep | awk '{print $$2}' | xargs kill  