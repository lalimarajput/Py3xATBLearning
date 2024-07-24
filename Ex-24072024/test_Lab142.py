import pytest  # pip install pytest
import allure  # pip install allure-pytest
import requests


@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Pramod Dutta")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200


@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#2 -> Verify that GET Request with invalid bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404



