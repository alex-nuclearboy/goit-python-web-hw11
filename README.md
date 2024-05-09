# Contact Management API

This repository contains a REST API for managing contact information, built with FastAPI and SQLAlchemy. 
It leverages PostgreSQL as the backend database and includes features such as creating, retrieving, updating, and deleting contact information. 
Additional functionalities include searching for contacts and retrieving contacts with upcoming birthdays.

## Features
- **Create new contacts:** Add new contact entries to the database.
- **Retrieve all contacts:** Fetch all contacts with pagination support.
- **Retrieve a single contact by ID:** Get details of a specific contact.
- **Update existing contacts:** Modify details of existing contacts.
- **Delete contacts:** Remove contact entries from the database.
- **Search for contacts:** Look up contacts by name, email, or phone number.
- **List upcoming birthdays:** Get contacts whose birthdays occur within the next week.

## Technologies Used

- **FastAPI:** For creating the REST API.
- **SQLAlchemy:** As the ORM for database interactions.
- **PostgreSQL:** As the backend database.
- **Pydantic:** For data validation.
- **Alembic:** For database migrations.
- **Docker:** Used to containerize the application and PostgreSQL database.
- **Poetry:** For managing Python package dependencies and virtual environments.

## Installation and Usage

### Prerequisites

- **Docker and Docker Compose:** Ensure you have Docker and Docker Compose installed on your system to handle the application and database containers.
- **Python:** Ensure Python 3.10 or higher is installed on your system.
- **Poetry:** This project uses Poetry for dependency management. Install Poetry by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

### Setting Up the Project

- **Clone the Repository:**
```bash
git clone https://github.com/alex-nuclearboy/goit-python-web-hw11.git
```

- **Navigate to the Project Directory:**
```bash
cd goit-python-web-hw11
```

- **Activate the Poetry Environment and Install Dependencies:**
```bash
poetry shell
poetry install --no-root
```

- **Start the PostgreSQL Server:**
```bash
docker compose up -d
```

- **Run Alembic Migrations**
```bash
alembic upgrade head
```

### Starting

- **Running the FastAPI application** using Uvicorn:
```bash
uvicorn main:app --host localhost --port 8000 --reload
```

This command will start the API server accessible at [http://localhost:8000](http://localhost:8000).

## API Documentation

Once the server is running, you can access the Swagger UI to test the API endpoints at [http://localhost:8000/docs](http://localhost:8000/docs).

## Stopping the Application and Exiting

When you are finished using the application, follow these steps to properly shut down the server and exit the development environment:

- **Stopping the Application:**

To stop the FastAPI application, you simply need to press `CTRL+C` in the terminal window where the server is running. This will terminate the server process.

- **Shutting Down the PostgreSQL Server:**

If you've started the PostgreSQL server using Docker Compose and wish to stop it, you can use the following command:
```bash
docker compose down
```

This command stops the running containers and removes the containers created by docker compose up, along with their networks. It’s a clean way to ensure that no unnecessary Docker processes remain running. If you wish to stop the container but not remove it, you can use:
```bash
docker compose stop
```

- **Exiting the Poetry Environment**
```bash
exit
```

This command will deactivate the virtual environment and return you to your system's default environment.
