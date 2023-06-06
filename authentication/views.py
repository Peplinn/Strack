from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import json
from json import JSONDecodeError
from django.http import JsonResponse

# Create your views here.
class UsernameValidationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['username']

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
        except KeyError:
            return JsonResponse({'error': 'Invalid request. "username" parameter is missing.'}, status=400)

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters.'}, status = 400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Username already in use. Choose another.'}, status = 409)
        

        return(JsonResponse({'username_valid': True}))



class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')