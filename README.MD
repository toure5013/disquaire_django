BISMILAHI RAHMANI RAHIM
ALAHOUMA SOLI ALA MOUHAMADIN WA ALA ALI MOUHAMADIN WA SALIM

1- project and app creation
-create your project 
django-admin startproject project_name

-create your apps 
django-admin startapp app_name
    config : in your project folder
        in settings.py  add 'folder_name.apps.appsNameConfig' in INSTALLED_APPS array

2 - database

-install your databse package 
example for mysql : 
pip install mysql

-setting your database
in setting file, add your database configuration inside DATABASES array
example for mysql : 
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
        'NAME': 'disquaire',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },
    
} 


-make migration
python manage.py migrate


4-config routes
import the url in django.conf.urls and wrire your urls

urlpatterns = [
    url(r'^$', views.index), #"/store" will call the method "index" in "views.py"
    url(r'^store/', include('store.urls')), #import a routes files from store app
    url(r'^admin/', admin.site.urls),
]


4-Run server 


4- admin"# disquaire_django" 
