from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Item
from .form import ItemForm

# Create your views here.
# home view or index default

# def index(request):
#     #get data fron databae
#     item_list = Item.objects.all()
#     return HttpResponse(item_list)

# def index(request):
#     # return a responase a html file from templetes
#     template = loader.get_template('food/index.html')
#     # we pass some context to that templete file empty or data from database
#     item_list = Item.objects.all()
#     context = {
#         'items' : item_list,
#     }
#     return HttpResponse(template.render(context,request))

# without httpresponce
def index(request):
    item_list = Item.objects.all()
    context = {
        'title' : 'Home',
        'items_list' : item_list,
    }
    return render(request,'food/index.html',context)


# add functionality that if we click on any item from home page it take us to 
# that item detail page, we go to detail page using item_id for that we create
# a detail function a pass id and in url also add that id so it goes to that item detail

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'title' : 'Detail',
        'item' : item,
    }
    return render(request,'food/detail.html',context)


def create_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    context ={
        'title' : 'Add New Item',
        'form' : form
    }
    return render(request,'food/item_form.html',context)


def edit_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance = item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context ={
        'title' : 'Edit Item',
        'form' : form,
        'item' : item,
    }
    return render(request,'food/item_form.html',context)

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    context ={
        'title' : 'Delete Item',
        'item' : item,
    }
    return render(request,'food/item_delete.html',context)
    




def greet(request,name):
    return HttpResponse(f'Hello {name}!')
def xyz(request):
    return HttpResponse(f'Hello AAQIb!')







