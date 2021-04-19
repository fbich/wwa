from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import os
import csv
from django import template
register = template.Library()

def index(request):

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'C:\DDATA\QuEstCeQuOnMange\AppFiles\WWA_TABLDC1.csv')   #full path to text.
    data_file = open(file_path , 'r')       
    data = data_file.read()
    print(data)

    MyFilename = 'D:/FBWebDev/WWA_TABLDC1.csv'
    print (MyFilename)

    with open(MyFilename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                myinglist = '|'.join(row)
                #myinglist = 'turlututu'
                print (myinglist)
                line_count += 1
            else:
                print(f'{", ".join(row)}')
                line_count += 1
        print(f'Processed {line_count} lines.')

    template = loader.get_template('index.html')
    context = {
        'nom' : 'Albert', 'age' : '12', 
        'materielinfo' : {'laptop' , 'Ipad' , 'imprimante' , 'chaise'},
        'Skills' : data,
        'inglist' : myinglist,
    }
    return HttpResponse(template.render(context, request))

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)