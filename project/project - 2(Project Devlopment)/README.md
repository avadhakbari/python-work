# work-book
work-book


1]  create repositories on github and clone in local system
>>> git init
>>>git clone https://<your-username>:<your-token>@github.com/avadhakbari/work-book.git

>>>cd work-book


2] create vartual environment of base directory
>>>...work-book> python -m venv <your environment name>


3] activate your virtual environment 
>>>...work-book> <your environment name>\Scripts\activate


also you deactivate your venv environment
>>>(your environmet name) ...work-book > <your environment name>\Scripts\deactivate.bat


4] create one text file
>>>(your environmet name) ...work-book > type nul > requirments.txt


5] make sure you have already installed python 
>>>(your environmet name) ...work-book >python --version 
>>>ans:- Python 3.12.2


6] now, install django
>>>(your environmet name) ...work-book > pip install django==1.2.3


7] chek installed packages and modules  in virtual environment 
>>>(your environmet name) ...work-book >pip list \ pip freeze
>>>ans:-
Package  Version
-------- -------
asgiref  3.8.1
Django   5.0.6
pip      24.0
sqlparse 0.5.0
tzdata   2024.1


8] add packeges and module in requirments.txt file 
>>>(your environmet name) ...work-book > pip freeze > requirment.txt


9] install and upgrade packeges and module according to txt file
>>>(your environmet name) ...work-book > pip install -r requirments.txt


10] make sure  you have installed django
>>> (your environmet name) ...work-book > python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.get_version()
'5.0.6'


11] create django app 
>>>(myvenv) C:\Users\Admin\work-book> django-admin startproject <your project_name>.


12] create django app 
>>>(myvenv) C:\Users\Admin\work-book> python manage.py startapp <your app_name>

Add app-name :
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'master' # add new
]



13] migrate your base-dir for create table into the admin site
>>>(myvenv) C:\Users\Admin\work-book> python manage.py makemigrations
>>>(myvenv) C:\Users\Admin\work-book> python manage.py migrate


14] create your superuser
>>>(myvenv) C:\Users\Admin\work-book> python manage.py createsuperuser


15] run your server
>>>(myvenv) C:\Users\Admin\work-book> python manage.py runserver

