from config.settings.base import DJANGO_ROOT
from django.shortcuts import render
import json
import os.path
import datetime

datafile_path = os.path.join(DJANGO_ROOT, "data", "messages.json")
with open(datafile_path) as json_file:
    all_message_list = json.load(json_file)
    all_message_list.sort(key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d') ,reverse=True)


def home(request):
    message_teaser= get_teasers(all_message_list)
    context_dict = {'message_details': message_teaser,
                    'menu': get_menu(),
                    'actual_slug' : 'home'
                    }

    return render(request, 'starter_app/home.html', context_dict)

def onepost(request, slug_tag):

    blogpost = [x for x in all_message_list if x['slug'] == slug_tag][0]

    context_dict = {'post':blogpost,
                    'menu':get_menu(),
                    'actual_slug' : slug_tag}
    return render(request, 'starter_app/post.html', context_dict)



def get_menu():

    return  [ {'slug':x['slug'],'title': x['title']} for x in all_message_list]


def get_teasers(message_list):
    message_teaser=[]
    for post in message_list:
        truncaded_post=dict()
        for key in post.keys():
            if key =="content" and len(post[key])>80:
                truncaded_post[key]=post[key][0:80]
            else:
                truncaded_post[key]=post[key]
        message_teaser.append(truncaded_post)
    return message_teaser