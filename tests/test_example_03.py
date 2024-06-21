import requests
import uuid

def create_post():
    return {
        "title": "The title of my new post",
        "body": "A very long string containing the body of my new post",
        "userId": 1
    }

def test_create_post():
    api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUmVzdFJ1biIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2hhc2giOiI0MjI4MjIwMC03OWYzLTRmN2UtOGI3ZS1jYjgyNGFkZGU2YzEiLCJzdWIiOiJQb3dlclNoZWxsVW5pdmVyc2FsIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiRXhlY3V0ZSIsIm5iZiI6MTY0OTM2NDk3NSwiZXhwIjoyMTA3Mjg0OTYwLCJpc3MiOiJJcm9ubWFuU29mdHdhcmUiLCJhdWQiOiJQb3dlclNoZWxsVW5pdmVyc2FsIn0.6Df6PZRdipuILPQRNCGy43_ZsBYtSmAHmwB0Vz-IS7s'
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=create_post(), auth=api_token)
    assert response.status_code == 201
    print(response.status_code == 201)
    assert isinstance(response.json()["id"], int) is True
    print(isinstance(response.json()["id"], int) is True)


def create_billpay_for(name):

    return {
      "name": name,
      "address": {
        "street": "My street",
        "city": "My city",
        "state": "My state",
        "zipCode": "90210"
      },
      "phoneNumber": "0123456789",
      "accountNumber": 12345
    }

def test_post_create_billpay_using_random_name():
    unique_name = str(uuid.uuid4())
    json_object = create_billpay_for(unique_name)
    response = requests.post(
        "https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500",
        headers={"Accept": "application/json"},
        json=json_object
    )

    assert response.status_code == 200
    print(response.status_code == 200)

    assert response.json()["payeeName"] == unique_name
    print(response.json()["payeeName"] == unique_name)