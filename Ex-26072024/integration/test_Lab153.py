# 2) Create a booking, Delete the booking with that id, Verify the GET request that it should not exist:

import allure  # pip install allure
import pytest  # pip install pytest
import requests  # pip install requests


@allure.title("Restful Booker Project-Integration Test Cases")
@allure.description("TC3-> Verify that create-booking -> DELETE Booking -> Verify that it is deleted")
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


def create_booking():
    # Booking ID
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the response Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)


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
