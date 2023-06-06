from django.shortcuts import render
from .models import Category, Project
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
# from userpreferences.models import UserPreference

# Create your views here.

def search_projects(request):
    if request.method=='POST':
        search_str = json.loads(request.body).get('searchText', '')

        projects = Project.objects.filter(
            amount__istartswith = search_str, owner = request.user) | Project.objects.filter(
            date__istartswith = search_str, owner = request.user) | Project.objects.filter(
            description__icontains = search_str, owner = request.user) | Project.objects.filter(
            category__icontains = search_str, owner = request.user)

        data = projects.values()

        return JsonResponse(list(data), safe=False)

@login_required(login_url='/authentication/login')
def index(request):
    categories = Category.objects.all()
    projects = Project.objects.filter(owner = request.user)
    paginator = Paginator(projects, 4)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    # currency = UserPreference.objects.get(user = request.user).currency
    context = {
        'projects' : projects,
        'page_obj' : page_obj,
        # 'currency' : currency
    }
    return render(request, 'expenses/index.html', context)

@login_required(login_url='/authentication/login')
def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'values' : request.POST
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        
        if not amount:
            messages.error(request, 'Amount is required.')
            return render(request, 'expenses/add_expense.html', context)

        description = request.POST['description']
        date = request.POST['listing_date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'Description is required.')
            return render(request, 'expenses/add_expense.html', context)
        
        if not date:
            messages.error(request, 'Date is required.')
            return render(request, 'expenses/add_expense.html', context)

        Project.objects.create(owner = request.user, amount = amount, date = date, category = category, description = description)
        
        messages.success(request, 'Project saved successfully!')

        return redirect('expenses')
    

def expense_edit(request, id):
    project = Project.objects.get(pk = id) #INCREMENTS DONE AUTOMATICALLY USING pk
    categories = Category.objects.all()

    context = {
        'project' : project,
        'values' : project,
        'categories' : categories, 
    }
    if request.method == 'GET':
        
        return render(request, 'expenses/edit-expense.html', context)
    if request.method == 'POST': 
        amount = request.POST['amount']
        
        if not amount:
            messages.error(request, 'Amount is required.')
            return render(request, 'expenses/edit-expense.html', context)

        description = request.POST['description']
        date = request.POST['listing_date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'Description is required.')
            return render(request, 'expenses/edit-expense.html', context)
        
        if not date:
            messages.error(request, 'Date is required.')
            return render(request, 'expenses/edit-expense.html', context)
        
        project.owner = request.user
        project.amount = amount
        project.date = date
        project.category = category
        project.description = description

        project.save()
        messages.success(request, 'Project updated successfully!')

        return redirect('expenses')

        messages.info(request, 'Handling post form.')
        return render(request, 'expenses/edit-expense.html', context)


def delete_expense(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    messages.success(request, 'Project removed.')
    return redirect('expenses')



