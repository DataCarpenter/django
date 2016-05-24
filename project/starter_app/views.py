from config.settings.base import DJANGO_ROOT
from django.shortcuts import render
import json
import os.path
import datetime
import copy

def read_json():
    datafile_path = os.path.join(DJANGO_ROOT, "data", "messages.json")
    with open(datafile_path) as json_file:
        all_message_list = json.load(json_file)
        for list_item in all_message_list:
            list_item['date'] = datetime.datetime.strptime(list_item['date'], '%Y-%m-%d')
        all_message_list.sort(key=lambda x: x['date'] ,reverse=True)
    return all_message_list


def home(request):
    teaser_list = copy.deepcopy(all_message_list)
    for post in teaser_list:
        if len(post["content"]) > 80:
            post["content"] = post["content"][0:80]

    context_dict = {'message_details': teaser_list,
                    'menu': get_menu(),
                    'actual_slug': 'home'
                    }

    return render(request, 'starter_app/home.html', context_dict)


def onepost(request, slug_tag):
    blogpost = find_blogpost(slug_tag)

    context_dict = {'post':blogpost,
                    'menu':get_menu(),
                    'actual_slug' : slug_tag}
    return render(request, 'starter_app/post.html', context_dict)


def get_menu():
    return  [{'slug':x['slug'],'title': x['title']} for x in all_message_list]


def find_blogpost(slug):
    for post in all_message_list:
        if post['slug'] == slug:
            return post

all_message_list = read_json()
