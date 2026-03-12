from fastapi.testclient import TestClient

from main import root, app

client = TestClient(app)

def test_base():
    with open("README.md", "r") as readme:
        readme_content = readme.read()

    base = client.get("/")

    assert base.status_code == 200
    assert base.json() == {"info about the project": readme_content}

def test_register():
    response = client.post("/register", json={"username": "testuser", "password": "Test1234"})

    assert response.status_code == 201
    assert response.json() == {"message": "User testuser registered successfully!"}

    response = client.post("/register", json={"username": "existing_user1", "password": "Test1234"})
    assert response.status_code == 409

    response = client.post("/register", json={"username": "newuser", "password": "short"})
    assert response.status_code == 400