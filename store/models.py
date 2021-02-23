from django.db import models

# Create your models here.

ARTISTS  = { 
    'francis-cabrel'  : {'name' : 'francis-cabrel'},
    'lej' : {'name' : 'elij'},
    'sam' : {'name' : 'mt-sams'},
}


ALBUMS = [
    {'name' : 'Sarbacae', 'artists' : ARTISTS['francis-cabrel']},
    {'name' : "La Dalle", 'artists' : ARTISTS['lej']},
    {'name' : "Valey", 'artists' : ARTISTS['sam']},
]