# Note Taking App Backend

## Overview

The Note Taking App Backend is a Django REST Framework-based backend for managing notes. It provides functionalities for user registration, authentication using JWT tokens, and note management.

## Features

- **User Registration:** Users can register for an account.
- **Login with Password:** Users can log in using their password.
- **Login with OTP:** Users can log in using a one-time password (OTP).
- **JWT Authentication:** The system uses JWT (JSON Web Token) for secure authentication.
- **Add Notes:** Users can add, update, and delete notes.

## Installation

Follow these steps to set up and run the project:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rishabh2030/note_taking_app_backend.git
   cd note_taking_app_backend
2. **Create and activate a virtual environment;**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
4. **Run the database migrations:**
    ```bash
    make migrate
5. **Create a superuser (optional, for admin access):**
    ```bash
    make createsuperuser (optional, for admin access):
    ```
## Usage
- **To start the development server, use:**
     ```bash
    make run
    ```
## Commands
The Makefile includes the following commands:

- **make migrate**: Apply database migrations.
- **make createsuperuser**: Create a Django superuser.
- **make run**: Start the development server.

## API docs
## API docs
- [swagger](http://127.0.0.1:8000/swagger/)
- [redoc](http://127.0.0.1:8000/redoc/)
