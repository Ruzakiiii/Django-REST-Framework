
first step:

---pip install django

second step:

---pip intsall djangorestframework

third step:

---django-admin startproject NAME .

fourth step:

---django-admin startapp NAME 

sixth step:

in file settings in INSTALLED_APPS add 'rest_framework'

seventh step:

in your app add directory serializers.py

eighth step:

then in file serializers.py add import from rest_framework import serializers and create class and inherit (serializers.ModelSerialize)
