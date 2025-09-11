import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Balance Service" in response.json().get("message", "")

def test_get_balance():
    account_id = 1
    response = client.get(f"/balance/{account_id}")
    assert response.status_code in [200, 404]  

def test_update_balance():
    account_id = 1
    payload = {"amount": 100.0}
    response = client.put(f"/balance/{account_id}", json=payload)
    assert response.status_code in [200, 404]
