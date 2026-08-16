import allure
import requests


BASE_URL = "http://localhost:8000"


@allure.title("Check health endpoint")
def test_health() -> None:
    url = f"{BASE_URL}/health"

    with allure.step("Send GET request"):
        response = requests.get(url)

    with allure.step("Attach response body"):
        allure.attach(
            response.text,
            name="Response body",
            attachment_type=allure.attachment_type.JSON,
        )

    with allure.step("Check response status code"):
        assert response.status_code == 200

    with allure.step("Check response body"):
        assert response.json() == {"status": "healthy"}