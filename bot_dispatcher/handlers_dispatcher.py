"""
Handler - функция, которая принимает на вход text (такст входящего сообщения) и context (dict), а возвращает bool:
True если шаг пройден, False если данные введены неправильно.
"""
import re

re_departure_city = re.compile(r'^[\w\-\s]{1,40}$')
re_arrival_city = re.compile(r'^[\w\-\s]{1,40}$')
re_date = re.compile(r"\d{1,2}-\d{1,2}-\d{4}")
re_flight = re.compile(r"\d{4}")
re_telephone = re.compile(r"\d{11}")

from bot_dispatcher.settings_dispatcher import CITY


def city_check(city):
    city_lower = city.lower()
    if city_lower == 'питер':
        return "Санкт-Петербург"
    wrong_characters = 2
    correct_letters = 0
    variant = []
    for correct_city in CITY:
        correct_city_lower = correct_city.lower()
        letter_match = 0
        if correct_city_lower[:-1] == city_lower[:-1]:
            return correct_city

        if correct_city_lower in city_lower or city_lower in correct_city_lower:
            if len(city_lower) > 3:
                print(2)
                return correct_city
            else:
                variant.append(correct_city)

        min_len = min(len(correct_city_lower), len(city_lower))

        for i in range(min_len - 1):
            if city_lower[i] in correct_city_lower[i]:
                letter_match += 1
        if letter_match >= len(correct_city_lower)-wrong_characters:
            variant.append(correct_city)

    variant = set(variant)
    variant = list(variant)

    if len(variant) == 1:
        variant = variant[0]
    return variant


def handler_departure_city(text, context):
    match = re.match(re_departure_city, text)
    if match and city_check(text):
        variant = city_check(text)
        if type(variant) != list or len(variant) == 1:
            context["departure_city"] = variant

            return True
        text = ''
        for v in variant:
            text += str(v) + '\n'
        context["var"] = text
    else:
        text = ''
        for v in CITY:
            text += str(v) + '\n'
        context["var"] = text
        return False


def handler_arrival_city(text, context):
    match = re.match(re_departure_city, text)
    if match and city_check(text):
        variant = city_check(text)
        if type(variant) != list or len(variant) == 1:
            context["arrival_city"] = variant

            return True
        text = ''
        for v in variant:
            text += str(v) + '\n'
        context["var"] = text
    else:
        text = ''
        for v in CITY:
            text += str(v) + '\n'
        context["var"] = text
        return False


def handler_date(text, context):
    match = re.match(re_date, text)
    if match:
        context["date"] = text
        return True
    else:
        return False


def handler_true(text, context):
    return True


from bot_dispatcher.settings_dispatcher import ALL_FLY_NUMBERS


def handler_flight_selection(text, context):
    match = re.match(re_flight, text)
    if match and int(text) in ALL_FLY_NUMBERS:
        context["flight"] = text
        return True
    else:
        return False


def handler_comment(text, context):
    context["comment"] = text
    return True


def handler_right(text, context):
    if text.lower() in ['да', "нет"]:
        context["right"] = True if text.lower() == 'да' else False
        print("context['right'] = ", context["right"])
        return True
    else:
        return False


def handler_telephone(text, context):
    match = re.match(re_telephone, text)
    if match:
        context["telephone"] = text
        return True
    else:
        return False


