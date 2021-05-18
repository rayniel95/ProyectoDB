__author__ = 'LsW'
from django.core import validators

def IntLenValidator(number):
    if len(str(number)) != 11:
        raise validators.ValidationError('El numero del CI debe tener longitud 11')
