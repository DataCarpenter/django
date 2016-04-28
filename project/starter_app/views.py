from config.settings.base import DJANGO_ROOT
from django.shortcuts import render
import json
import os.path

datafile_path = os.path.join(DJANGO_ROOT, "data", "messages.json")
with open(datafile_path) as json_file:
    json_data = json.load(json_file)


def home(request):

    #messages = Message.objects.order_by('order')
    
    posts= [x['post'] for x in json_data]
    context_dict = {'messages': posts}
    return render(request, 'starter_app/home.html', context_dict)

def onepost(request):

    post_name= request.path_info[1:]
    blogpost = [x for x in json_data if x['post']== post_name]

    context_dict = blogpost[0]
    return render(request, 'starter_app/post.html', context_dict)
