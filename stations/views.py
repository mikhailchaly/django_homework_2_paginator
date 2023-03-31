from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    with open("data-398-2018-08-30.csv", 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        my_list = list(reader)
        my_list.pop(0)
        _dict = {}
        list_of_dict = []

        for elem in my_list:
            _dict = dict(Name=elem[1], Street=elem[4], District=elem[6])
            list_of_dict.append(_dict)
            _dict = {}

    CONTENT = list_of_dict
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)

    context = {
            'bus_stations': page,
            'page': page,
            }

    return render(request, 'stations/index.html', context)
