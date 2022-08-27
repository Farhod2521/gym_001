from atexit import register
from django import template


import datetime

register = template.Library()

@register.filter(name="in_data")
def in_data(i):
    b = int(i.data.strftime("%Y%m%d"))
    today = datetime.datetime.now()
    print(b)
    print("####################################")
   
     
    c = int(today.strftime("%Y%m%d"))
    print(c)
    otgan_oy = int(i.data.strftime("%m"))
    hozirgi_oy = int(today.strftime("%m"))
    if otgan_oy < hozirgi_oy:
        return c-b-70
    else:   
        return c-b