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
```bash
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








