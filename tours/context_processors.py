departures_ = {
    "msk": "Из Москвы",
    "spb": "Из Петербурга",
    "nsk": "Из Новосибирска",
    "ekb": "Из Екатеринбурга",
    "kazan": "Из Казани",
}


def departures(request):
    return {'departures': departures_.items()}
