import httpx

login_payload = {
    "email": "user@example2221.com",
    "password": "password"
}
user_data = {
    "user": {
        "id": "56b893b7-8198-4305-a198-2e5991d82322",
        "email": "user@example2221.com",
        "lastName": "lolo",
        "firstName": "ololo",
        "middleName": "ololoevich"
    }
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

assert login_response.status_code == 200, f"Статус код {login_response.status_code} ошибочно отличается от ожидаемого"
assert "token" in login_response_data, "Ответ не содержит поле 'token'"
assert "accessToken" in login_response_data["token"], "Токен не содержит поле 'accessToken'"

access_token = login_response_data["token"]["accessToken"]

user_me_response = httpx.get(
    url="http://localhost:8000/api/v1/users/me",
    headers={"Authorization": f"Bearer {access_token}"}
)
assert user_me_response.status_code == 200, f"Статус код {user_me_response.status_code} ошибочно отличается от ожидаемого"
assert user_me_response.json() == user_data, 'Данные в ответе ошибочяно отличаются от ожидаемых'
