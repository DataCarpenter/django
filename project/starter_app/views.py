from config.settings.base import DJANGO_ROOT
from django.shortcuts import render
import json
import os.path

datafile_path=os.path.join(DJANGO_ROOT,"data","messages.json")
with open(datafile_path) as json_file:
    json_data = json.load(json_file)


def home(request):
    
    #messages = Message.objects.order_by('order')
    
    context_dict = { 'messages': json_data['posts'] }
    return render(request, 'starter_app/home.html', context_dict)
