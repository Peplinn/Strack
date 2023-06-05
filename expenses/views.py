from django.shortcuts import render
from .models import Category, Project
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    categories = Category.objects.all()
    projects = Project.objects.filter(owner = request.user)

    context = {
        'projects' : projects
    }
    return render(request, 'expenses/index.html', context)

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



