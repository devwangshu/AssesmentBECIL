## How to run the Project on Ubuntu 20.04 LTS/or latest earlier


	Step 1: Open Ubuntu Terminal (ctrl+alt+T)


---------------------------Ubuntu commands Virtual env setup-----------------

	Step 2: python3  -V ##check the python version

	Step 3: sudo apt install python3 -venv ## install virtual env for 1st time

	Step 4: python3 m venv myproject_env ##create env a/c to project , particulat location

	Step 5: source myproject_env/bin/activate ##activate the virtual environment

	deactivate ##command for deactivate the environment

	Step 6:pip3 install Django  ##to install django in active vir enviroment

	Step 7:pip install library_name  ##to install any library like requests

	Step 8:pip install -r requirements.txt ## install all libarry once in single file 

	Step 9: pip freeze ## to see the list of library under the vir env

	Setp 10: pip freeze >requirements.txt ## export all installed library list in this text file

-----------------Run Django Project on virtual env on Ubuntu-------------------------------

	source myproject_env/bin/activate




	python3 manage.py runserver   ##run your project on localhost:8000

	python3 managae.py createsuperuser  ##to create admin login (django)

	python manage.py makemigrations  ##create migrations files

	python3 manage.py migrate  ##to migrate database tables

## How to run the Project on Windows:

	Step 1: Install Python 3.x

	Step 2: pip install virtualenvwrapper-win # first time only

	Step 3: mkvirtualenv myproject ##you can change myproject to anything

	Step 4 :workon myproject

	Step 5 :pip install -r requirements.txt

	Step 6: python managae.py createsuperuser 

	Step 7: python manage.py makemigrations 

	Step 8: python3 manage.py runserver 

	Step 10: Open Browser and type localhost:8000 or 127.0.0.1:8000
