from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreference
from django.contrib import messages

# Create your views here.

def index(request):

    currency_data = []

    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

        for k,v in data.items():
            currency_data.append({'name': k, 'value': v})
    # import pdb
    # pdb.set_trace()
    return render(request, 'preferences/index.html', {'currencies': currency_data})

