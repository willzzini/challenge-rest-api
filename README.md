# serasa-rest-api [![Build Status](https://travis-ci.org/gitgik/flask-rest-api.svg?branch=master)](https://travis-ci.org/gitgik/flask-rest-api)
A flask-driven restful API for information analysis


## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
 over others.
* Minor dependencies can be found in the requirements.txt file on the root folder.


## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC
    ```
        $ git clone https://github.com/willzzini/serasa-rest-api.git
    ```


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd serasa-rest-api
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv venv --python=python3.5
        $ source venv/bin/activate
        ```

* #### Install your requirements
    ```
    (venv)$ pip freeze
    ```

* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ rm data.db
    (venv)$ python app.py
    ```
    You can now access the app on your local browser by using
    ```
    http://127.0.0.1:5000/
    ```
    Or test creating data using Postman
