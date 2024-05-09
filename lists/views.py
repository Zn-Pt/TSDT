# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from lists.models import Item
#
#
# def home_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/')
#
#     items = Item.objects.all()
#     return render(request, 'home.html',{'items': items})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-new-page/')
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, "list.html", {'items': items})

def new_list(request):
    list_user = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_user)
    return redirect('/lists/the-new-page/')