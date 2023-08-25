# User_Management_System



# README FILE

The Project is Done using Django and Django rest FrameWork 
I have Created a backend of the project. The apis can be integrated the frontend can be implemented with any advance Frameworks like Angular or React

DO Read api_list.text to list all the apis


Key Features
 Markup : 
*Jwt authentication ,
*User Login and registration ,
*Throttling ,
*Rest Apis ,
*cros headers ,


Note - For windows user use python for linux user use python3 while running the commands.( I have used linux (ubuntu) )




#####################  Project Installations ######################


# If using virtual env activate it then run the following command inside the project

	pip3 install -r requirements.txt


# In settings.py file change the following accordingly to your preference


EMAIL_HOST_USER = '------'  # email
EMAIL_HOST_PASSWORD  ='-------' # password




# cd inside Project Where manage.py file is located

	python3 manage.py makemigrations
	python3 manage.py migrate


# To create a admin user 

	python3 manage.py createsuperuser

# To runserver

	python3 manage.py runserver


# Project is running Now :)


# POSTMAN API Docmentation

https://api.postman.com/collections/29347056-d20de209-9883-405d-a8f8-b4ca24362e1e?access_key=PMAT-01H8PGXS7JNY0Z21RRGBY47CYQ
