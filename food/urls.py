from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    # default or index page
    path('',views.index,name='index'),
    # view detail with id 
    path('<int:item_id>/',views.detail,name='detail'), 
    # add item
    path('add/',views.create_item,name='create_item'),
    
    
    
    
    
    #placeholder url
    path("xyz/",views.xyz,name="xyz"), # place holder without/ while a pageor a different view with a / othervise it is considered as a string
    path("<str:name>",views.greet,name="greet"),  #name same as greet argument
    
    # edit item with id
    path('edit_item/<int:id>',views.edit_item,name="edit_item"),
    # delete item with id
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    
    ]