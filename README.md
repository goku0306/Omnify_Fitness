# Omnify_Fitness.API

A FastAPI-based backend application for managing fitness-related operations such as class bookings, client data, and more.

---

## Requirements

- Python 3.8+
- MS SQL Server
- `pip` for Python package management

---



Install all the requirements from requirements.txt using

- pip install -r requirements.txt

# DB
- Make sure you've changed the DB connection URL. You can change DB connection URL in `./DBAccess/dbAccess.py`.
- Before running the application Create a DB with the name of 'FitnessDB'
- Once the application runs successfully table will be created to your DB automatically

To run the application
- uvicorn main:app --reload (or) python -m uvicorn main:app

