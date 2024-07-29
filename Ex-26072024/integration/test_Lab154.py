# 3) GET an existing booking from GET all booking id's , Update a booking with that id,
# Verify with GET request that it is updated

import allure  # pip install allure
import pytest  # pip install pytest
import requests  # pip install requests


@allure.title("Restful Booker Project-Integration Test Cases")
@allure.description("TC4-> Verify that Get-booking -> PUT request -> Verify that firstname is updated")
def create_token():
    # token
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200


def test_put_request_postive():
    URL = "https://restful-booker.herokuapp.com/booking/1"

    cookie = "token=" + create_token()

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Lily",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Lily"


def test_get_booking():
    URL = "https://restful-booker.herokuapp.com/booking/1"
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.patch(url=URL, headers=headers)
