import random

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from tours import data


# Create your views here.


def main_view(request):
    random_tours = random.sample(data.tours.items(), 6)
    return render(request, 'tours/index.html', {'tours': random_tours})


def departure_view(request, departure):
    tours = []

    for tour_id, tour in data.tours.items():
        if tour['departure'] == departure:
            tours.append((tour_id, tour))

    min_price = min([tour['price'] for tour_id, tour in tours])
    max_price = max([tour['price'] for tour_id, tour in tours])

    min_nights = min([tour['nights'] for tour_id, tour in tours])
    max_nights = max([tour['nights'] for tour_id, tour in tours])

    departure_name = data.departures[departure]

    return render(request, 'tours/departure.html', {'tours': tours,
                                                    'departure_name': departure_name,
                                                    'min_price': min_price,
                                                    'max_price': max_price,
                                                    'min_nights': min_nights,
                                                    'max_nights': max_nights})


def tour_view(request, tour_id):
    tour = data.tours[tour_id]
    hotel_stars = int(tour['stars']) * '★'
    departure = data.departures[tour['departure']]

    return render(request, 'tours/tour.html', {'tour': tour,
                                               'hotel_stars': hotel_stars,
                                               'departure': departure})


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 — страница не найдена.')


def custom_handler500(request):
    return HttpResponseServerError('500 — внутренняя ошибка сервера.')
