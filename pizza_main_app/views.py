from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Menu, Pizza, Sushi, Set

def sorting_list(lst: list, cols: int) -> list[list]:
    return [lst[i:i + cols] for i in range(0, len(lst), cols)]


def home(request):
    page_title = 'Pizza Shop'
    drop_menu = Menu.objects.all()
    pizza_all = Pizza.objects.all()
    sushi_all = Sushi.objects.all()
    sets_all = Set.objects.all()
    combined_all = list(pizza_all)+list(sushi_all)+list(sets_all)
    combined_result = sorting_list(combined_all, 3)
    return render(request, 'main.html', {'drop_items': drop_menu, 'combined_result': combined_result, 'global_title': page_title})

def pizza(request):
    page_title = 'All Pizza'
    drop_menu = Menu.objects.all()
    pizza_all = Pizza.objects.all()
    combined_result = sorting_list(pizza_all, 3)
    return render(request, 'main.html', {'drop_items': drop_menu, 'combined_result': combined_result, 'global_title': page_title})

def sushi(request):
    page_title = 'All Sushi'
    drop_menu = Menu.objects.all()
    sushi_all = Sushi.objects.all()
    combined_result = sorting_list(sushi_all, 3)
    return render(request, 'main.html', {'drop_items': drop_menu, 'combined_result': combined_result, 'global_title': page_title})

def sets(request):
    page_title = 'All Sets'
    drop_menu = Menu.objects.all()
    sets_all = Set.objects.all()
    combined_result = sorting_list(sets_all, 3)
    return render(request, 'main.html', {'drop_items': drop_menu, 'combined_result': combined_result, 'global_title': page_title})
