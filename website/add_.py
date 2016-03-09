#!/usr/bin/env python
import os
import sys
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
from django.contrib.auth.models import User

def make_passwd():
    words = 'the,man,cat,ball,make,dog,he,she,nuts,red,for,are,but,not,you'.split(',')
    needed = random.sample(words,3)
    return '-'.join(needed)



pass_list = []
with open('members.csv', 'r') as fl:
    for line in fl.readlines():
        name, email = line.split(',')
        password = make_passwd()
        u = User.objects.create_user(name, email, password)
        pass_list.append(','.join([name, password])+'\n')
with open('pass', 'w') as fl:
    fl.writelines(pass_list)
