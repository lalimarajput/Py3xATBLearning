#Integration Scenarios:-
# 1) Verify that create-booking -> patch request -> Verify that firstname is updated,.

import pytest
import allure
import requests


@allure.title("Restful Booker Project-Integration Test Cases")
@allure.description("TC2-> Verify that create-booking -> patch request -> Verify that firstname is updated")
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    response_data = response.json()
    token = response_data["token"]
    return token


def create_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-04-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=booking_url, headers=headers, json=payload)
    response_data = response.json()
    bookingid = response_data["bookingid"]
    return bookingid


def test_patch_request():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    url = base_url + str(create_booking())
    cookies = "token= " + create_token()
    headers = {"Content-Type": "application/json", "Cookie": cookies}
    payload = {
        "firstname": "Lee",
        "lastname": "Brown"
    }
    response = requests.patch(url=url, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Lee"


def test_get_booking():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    GET_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.patch(url=GET_URL, headers=headers)
