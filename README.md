# serasa-rest-api [![Build Status](https://travis-ci.org/gitgik/flask-rest-api.svg?branch=master)](https://travis-ci.org/gitgik/flask-rest-api)
A flask-driven restful API for information analysis


## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Docker](https://docs.docker.com/)** - Docker is a platform for developers and sysadmins to develop, deploy, and run applications with containers
 over others.
* Minor dependencies can be found in the requirements.txt file on the root folder.


## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed docker globally as well. If not, run this:
    ```
        $ sudo apt update
	$ sudo apt install docker.io
    ```
* Git clone this repo to your PC
    ```
        $ git clone https://github.com/willzzini/serasa-rest-api.git
    ````

* #### Running It
    Cd into your the cloned repo as such, run the server using this one simple command:
	
    ```
    $ docker build -t serasa-api .
    $ docker run -p 4000:80 serasa-api
    ```
    You can now access the app on your local browser by using
    ```
    http://127.0.0.1:4000/customers
    ```
    Or test creating data using Postman

* #### Postman Test
    1. In postman you should create an admi user with the endpoint:
        ```
        http://127.0.0.1:4000/register
        ```

    2. Then you will have to obtain a token so that it is possible to navigate the other endpoints:
        ```
        http://127.0.0.1:4000/auth
	```

    3. So that it is possible to access the endpoints it is necessary to pass in the Headers of postaman the JWT token space, see:
        ```
        JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiZXhwIjoxNTE5OTY4NDg5
		LCJuYmYiOjE1MTk5NjgxODksImlhdCI6MTUxOTk2ODE4OX0.Vls3yeH7ssOsTFHQJBCALRXihPjOGZqYekxrSpwxWoY
	```

