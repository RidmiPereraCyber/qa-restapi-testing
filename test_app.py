import pytest
from main import app, db, Destination

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # in-memory DB for tests
    with app.app_context():
        db.create_all()
        sample = Destination(Destination="Eiffel Tower", Country="France", rating=4.8)
        db.session.add(sample)
        db.session.commit()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Welcome to the travel API"


def test_get_destinations(client):
    res = client.get("/destinations")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 1
    assert data[0]["destination"] == "Eiffel Tower"


def test_get_single_destination(client):
    res = client.get("/destinations/1")
    assert res.status_code == 200
    data = res.get_json()
    assert data["country"] == "France"

def test_add_destination(client):
    res = client.post("/destinations", json={
        "destination": "Great Wall",
        "country": "China",
        "rating": 4.7
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["destination"] == "Great Wall"

def test_update_destination(client):
    res = client.put("/destinations/1", json={
        "destination": "Eiffel Tower Updated",
        "rating": 5.0
    })
    assert res.status_code == 200
    data = res.get_json()
    assert data["destination"] == "Eiffel Tower Updated"
    assert data["rating"] == 5.0

def test_delete_destination(client):
    res = client.delete("/destinations/1")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Destination was deleted"

    res = client.get("/destinations/1")
    assert res.status_code == 404
