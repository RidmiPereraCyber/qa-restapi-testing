# Travel Destinations REST API

A simple REST API built with Flask and SQLite for managing travel destinations.  
Supports full CRUD operations and includes both automated tests (pytest) and manual verification (Postman).  

---

## Features
- Add new travel destinations
- View all destinations or fetch by ID
- Update existing destinations
- Delete destinations
- Automated testing with pytest
- Manual testing with Postman

---

## Tech Stack
- Backend: Flask, SQLAlchemy  
- Database: SQLite  
- Testing: pytest, Flask test client  
- Manual Testing: Postman  

---

## Getting Started

### 1. Clone the repository
git clone https://github.com/your-username/qa-restapi-testing.git
cd qa-restapi-testing

### 2. Create the virrtual environment and install dependencies
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

### 3. Run the application

python main.py

## Available Endpoints (API)

| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| GET    | `/`                  | Welcome message       |
| GET    | `/destinations`      | Get all destinations  |
| GET    | `/destinations/<id>` | Get destination by ID |
| POST   | `/destinations`      | Add new destination   |
| PUT    | `/destinations/<id>` | Update a destination  |
| DELETE | `/destinations/<id>` | Delete a destination  |

# Manual Testing using "Postman"

-- Created a Postman collection
<img width="948" height="492" alt="image" src="https://github.com/user-attachments/assets/8468fa4f-8b42-4ce6-affb-d1c8024fc1f6" />

-- Configured base URL in Postman environment
<img width="835" height="292" alt="image" src="https://github.com/user-attachments/assets/b17fc324-67f5-4d98-b621-01cd7199c75c" />

## Test Cases

### Home Route
- Action: GET /
- Expected Result: Status 200 with message "Welcome to the travel API"
- Actual Result: Status 200 with message "Welcome to the travel API"

<img width="943" height="1006" alt="image" src="https://github.com/user-attachments/assets/568651fb-d097-4291-8552-3893a02f6a74" />

### Add New Destinations
- Action: POST /destinations with body:
**{
  "destination": "Eiffel Tower",
  "country": "France",
  "rating": 4.8
}**
- Expected Result: Status 201 with the created destination objec
- Actual Result: Status 201 with the created destination object

<img width="947" height="1008" alt="image" src="https://github.com/user-attachments/assets/2870bce9-2973-4f01-b49e-bcc15c302461" />

<img width="830" height="277" alt="image" src="https://github.com/user-attachments/assets/7633a6f5-ed32-48a2-a7dc-4759553b169e" />

<img width="841" height="245" alt="image" src="https://github.com/user-attachments/assets/3e679603-d307-4134-ad59-6c0c65e8b1d4" />

### Get all destinations
- Action: GET /destinations
- Expected Result: Status 200 with a list (possibly empty if no data)
- Actual Result: Status 200 with list of destinations

<img width="946" height="962" alt="image" src="https://github.com/user-attachments/assets/31bfb880-5a00-4228-bc63-517f87768ddc" />

### Get single Destination
- Action: GET /destinations/1
- Expected Result: Status 200 with destination object
- Actual Result: Status 200 with destination object

<img width="927" height="578" alt="image" src="https://github.com/user-attachments/assets/973832ac-f93b-4f60-a5b6-0f6a89c24db7" />

### Get Single Destination (Invalid ID)
- Action: GET /destinations/999
- Expected Result: Status 404 with error message "Destination not found"
- Actual Result: Status 404 with error message "Destination not found"

<img width="947" height="528" alt="image" src="https://github.com/user-attachments/assets/9e9e0eae-7bfb-4ce1-8265-3c5355944b77" />

### Update Destination
- Action: PUT /destinations/1 with body:
**{
  "destination": "Eiffel Tower Updated",
  "rating": 5.0
}**
- Expected Result: Status 200 with updated fields
- Actual Result: Status 200 with updated fields
<img width="938" height="821" alt="image" src="https://github.com/user-attachments/assets/34a10d1b-8bd1-4055-9745-957b47ce5c17" />

### Delete Destination
- Action: DELETE /destinations/1
- Expected Result: Status 200 with confirmation message
- Actual Result: Status 200 with confirmation message
<img width="957" height="496" alt="image" src="https://github.com/user-attachments/assets/ec4cba44-3221-4c59-9292-3b234b1d2182" />

### Delete Non-existing Destination
- Action: DELETE /destinations/999
- Expected Result: Status 404 with error message "Destination not found"
- Actual Result: Status 404 with error message "Destination not found"
<img width="955" height="482" alt="image" src="https://github.com/user-attachments/assets/1cbb9c4d-5749-4526-86a8-a21329623fea" />

# Pytest Unit Testing (Automated)
This Flask application includes unit tests using pytest to ensure that all API endpoints work correctly. The tests use Flask’s built-in test_client and an in-memory SQLite database to avoid modifying your actual database.

## How It Works

### Client Fixture

**@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    ...**   
    
- Sets the Flask app in testing mode.
- Uses an in-memory SQLite database for isolated tests.
- Creates a sample destination (Eiffel Tower) before running tests.
- Drops all tables after the tests to clean up.

### Test Home Route

**def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Welcome to the travel API"**

- Sends a GET request to /.
- Checks that the status code is 200.
- Validates the returned JSON message.
### Test Getting All Destinations
**
def test_get_destinations(client):
    res = client.get("/destinations")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 1
    assert data[0]["destination"] == "Eiffel Tower"**

- Sends a GET request to /destinations.
- Confirms the response contains the pre-populated destination.
### Test Getting a Single Destination
**
def test_get_single_destination(client):
    res = client.get("/destinations/1")
    assert res.status_code == 200
    data = res.get_json()
    assert data["country"] == "France"**

- Requests /destinations/1.
- Checks that the correct destination is returned.

### Test Adding a New Destination

**def test_add_destination(client):
    res = client.post("/destinations", json={
        "destination": "Great Wall",
        "country": "China",
        "rating": 4.7
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["destination"] == "Great Wall"**
    
- Sends a POST request to add a new destination.
- Validates that it is created successfully with status 201.

### Test Updating a Destination

**def test_update_destination(client):
    res = client.put("/destinations/1", json={
        "destination": "Eiffel Tower Updated",
        "rating": 5.0
    })
    assert res.status_code == 200
    data = res.get_json()
    assert data["destination"] == "Eiffel Tower Updated"
    assert data["rating"] == 5.0**

- Sends a PUT request to update an existing destination.
- Confirms the destination and rating are updated in the response.

### Test Deleting a Destination

**def test_delete_destination(client):
    res = client.delete("/destinations/1")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Destination was deleted"

    res = client.get("/destinations/1")
    assert res.status_code == 404**

- Deletes the destination at /destinations/1.
- Confirms deletion with a success message.
- Verifies that subsequent GET requests return 404.








