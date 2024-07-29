# 5) Invalid creation -  Enter a wrong payload or JSON:

import pytest
import allure
import requests


@allure.title("Restful Booker Project-Integration Test Cases")
@allure.description(
    "TC6-> Verify that create booking with invalid json")
def test_create_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111122223333444455556666777788899999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "245665786767",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=booking_url, headers=headers, json=json_payload)
    assert response.status_code == 500
    print(response)