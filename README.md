# chicken_backend
to setup Project on development env run following commands 

clone repo


`pip install -r requirements.txt `

configure  settings.py 

`python manage.py makemigrations`

`python manage.py migrate`

to run fixtures

`python manage.py loaddata fixtures/*.json`

to run server

`python manage.py runserver`



coding stardards for Project


    
`module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.`

*versions*

python 3.9 django4==0