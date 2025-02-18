# Some-Book-API
Hahaha
It's just another API.


> V1
### Note
This project has some areas that could be improved. Please feel free to read it and ignore any mistakes or workarounds. I plan to improve it in the future when I have more time.


## Commands
This handy guide will help you run projects and read documents:

1. Clone the project.
`````````
> git clone https://github.com/M-b850/Some-Book-API.git
> cd Some-Book-API/
`````````

> Ensure Python3 and Pip are correctly installed and functioning before proceeding to step 2.
> <br>
> Install virtualenv by running ``` pip3 install virtualenv ```
> <br>
> Install virtualenv by running [windows] ``` pip install virtualenv ```

2. Create virtualend and install requirements.
`````````
> virtualenv venv
> source venv/bin/activate
> pip install -r requirements.txt
`````````

2. Create virtualend and install requirements. [windows]
`````````
> virtualenv venv
> venv/Scripts/activate.bat
> pip install django
> pip install djangorestframework
> pip install -U drf-yasg
> pip install Pillow
> pip install django-cors-headers
`````````

3. Make migrations and create database.
`````````
> ./manage.py makemigrations
> ./mange.py migrate
`````````

3. Make migrations and create database. [windows]
`````````
> python manage.py makemigrations
> python mange.py migrate
`````````

4. Run server.
````````
> ./manage.py runserver
````````

4. Run server. [windows]
````````
> python manage.py runserver
````````

> Django runs its server on port `8000` by default. 
> You can run server on specific ports if you add port number after runserver command<br>
> example on port 9000: ``` ./manage.py runserver 9000 ``` <br>


## Shell Plus
````````
> ./manage.py shell_plus --ipython
````````

## Help

You can find Documentations here:
`````
localhost:port/swagger/
`````
> example:
> `` http://127.0.0.1:8000/swagger/ ``

## TODO
