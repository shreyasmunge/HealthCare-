

# 🏥 HealthCare Backend

A Django REST Framework-based backend system for managing patients, doctors, and mappings in a healthcare environment with secure JWT authentication.

---

## 🛠️ Installation

Follow the steps below to get the project running on your local machine.

### ⚙️ Prerequisites

Make sure you have the following installed:

* Python 3.10+
* pip (Python package installer)
* PostgreSQL (or use SQLite for local testing)
* Git
* Virtual environment tool (`venv` or `virtualenv`)

### 📦 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/shreyasmunge/HealthCare-.git
cd HealthCare-

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# Create a .env file and add your secrets (SECRET_KEY, DB settings, etc.)

# 5. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create a superuser
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
```

---

### 🔐 JWT Authentication

1. **Login to get access & refresh tokens:**

```bash
POST /api/auth/login/
{
  "email": "your-email@example.com",
  "password": "your-password"
}
```

2. **Use the access token in headers:**

```
Authorization: Bearer <your-access-token>
```

Sure! Here's your full **🧪 API Endpoints** section in **copy-paste ready format** — clean and consistent, like professional API documentation:

---

## 🧪 API Endpoints

### 1. 🔑 **Authentication**

```bash
POST    /api/auth/register/       # Register a new user
POST    /api/auth/login/          # Log in and get JWT tokens
POST    /api/auth/token/refresh/  # Get a new access token
```

---

### 2. 🩺 **Patient Management**

🔒 All patient APIs require JWT authentication.

```bash
POST    /api/patients/            # Add a new patient
GET     /api/patients/            # Get all patients created by the user
GET     /api/patients/<id>/       # Get details of a specific patient
PUT     /api/patients/<id>/       # Update a patient's information
DELETE  /api/patients/<id>/       # Delete a patient
```

---

### 3. 👨‍⚕️ **Doctor Management**

🔒 All doctor APIs require JWT authentication.

```bash
POST    /api/doctors/             # Add a new doctor
GET     /api/doctors/             # Retrieve all doctors
GET     /api/doctors/<id>/        # Get details of a doctor
PUT     /api/doctors/<id>/        # Update a doctor
DELETE  /api/doctors/<id>/        # Delete a doctor
```

---

### 4. 🔁 **Patient-Doctor Mapping**

🔒 All mapping APIs require JWT authentication.

```bash
POST    /api/mappings/                        # Assign a doctor to a patient
GET     /api/mappings/                        # Get all patient-doctor mappings
GET     /api/mappings/patient/<patient_id>/   # Get doctors assigned to a patient
DELETE  /api/mappings/<id>/                   # Delete a mapping
```

---

## 🧪 API Testing (Hoppscotch)

### ✅ Headers for Authenticated Requests

```bash
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

---

### 📦 Example: Create Patient (`POST /api/patients/`)

```json
{
  "name": "Shreyas",
  "age": 30,
  "disease": "Flu"
}
```

---

## ⚙️ Technologies Used

* [Django](https://www.djangoproject.com/) – Web framework used for backend development
* [Django REST Framework](https://www.django-rest-framework.org/) – Toolkit for building Web APIs
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) – For handling JWT authentication
* [PostgreSQL](https://www.postgresql.org/) – Relational database used for data storage
* [python-dotenv](https://pypi.org/project/python-dotenv/) – For managing environment variables securely
* [Hoppscotch](https://hoppscotch.io/) – For testing RESTful APIs

---

## 🤝 Contributing

Want to contribute? Here's how:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes and commit (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request
