# 🚀 Task Management API
> 📚 **Learning Project** — A RESTful API built to learn FastAPI fundamentals, including CRUD operations, request validation, and backend architecture.

## ✨ Features
- Create Task
- Get All Tasks
- Get Task by ID
- Update Task
- Delete Task
- Request Validation using Pydantic
- Automatic API Documentation (Swagger & ReDoc)

## 🛠️ Tech Stack
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (can be replaced with PostgreSQL/MySQL)
- Uvicorn
## 📁 Project Structure
```text
task_management_fastapi/
│
├── database.py
├── main.py
├── models/
│   └── task.py
├── routers/
│   └── task_router.py
├── schema/
│   ├── message.py
│   └── task.py
├── services/
│   └── task_service.py
├── requirements.txt
└── README.md
```
## ⚙️ Installation
### 1. Clone Repository
```bash
git clone https://github.com/dimasjayadi99/fast-api-python.git
cd fast-api-python
```
### 2. Create Virtual Environment
#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```
#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## ▶️ Run the Application
```bash
uvicorn main:app --reload
```
The API will be available at:
```
http://127.0.0.1:8000
```
## 📖 API Documentation

### Swagger UI
```
http://127.0.0.1:8000/docs
```
### ReDoc
```
http://127.0.0.1:8000/redoc
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/task/` | Get all tasks |
| GET | `/task/{id}` | Get a task by ID |
| POST | `/task/` | Create a new task |
| PUT | `/task/{id}` | Update an existing task |
| DELETE | `/task/{id}` | Delete a task |

## 📦 Example Request
### Create Task
**Request**
```http
POST /task/
Content-Type: application/json
```

```json
{
  "title": "Learn FastAPI",
  "description": "Build CRUD API",
  "is_completed": false
}
```

**Response**
```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "is_complete": true,
  "created_at": "2026-07-16T04:21:10.792Z",
  "updated_at": "2026-07-16T04:21:10.792Z",
  "user_id": 0
}
```

## 📈 Roadmap

- [x] CRUD Operations
- [ ] Request Validation
- [ ] Global Exception Handling
- [ ] JWT Authentication
- [ ] Authorization (Role-Based Access)
- [ ] Pagination
- [ ] Search & Filter
- [ ] Sorting
- [ ] Database Migration (Alembic)
- [ ] Docker
- [ ] Unit Testing
- [ ] CI/CD Pipeline
- [ ] Deployment
