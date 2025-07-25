# Secret Friend Application (Console)

This is a console application developed in Python to manage the dynamics of a Secret Santa game. It allows you to create users, groups, manage group participants, wish lists, and gifts, with data persistence in a PostgreSQL database.

## Features

The application offers the following functionalities, accessible through interactive console menus:

  * User Management
  * Group Management
  * Manage Group Users (Participants)
  * Manage a Participant's Wish Lists in a Group
  * Manage Gifts
  * Manage Letters
  * Terminate Program

## Prerequisites

Before running the application, ensure you have the following software installed:

  * **Python 3.x**
  * **PostgreSQL** (Database Server)
  * **psycopg2**: Python driver for PostgreSQL.
  * **Environment Variables**: Database access configurations.

## Database Configuration

The application connects to a PostgreSQL database. You will need to configure the following environment variables with your database credentials:

  * `DB_USER_PG`: PostgreSQL Username
  * `DB_PASSWORD_PG`: PostgreSQL Password
  * `DB_HOST_PG`: PostgreSQL Host (e.g., `localhost` or IP)
  * `DB_PORT_PG`: PostgreSQL Port (default: `5432`)
  * `DB_DATABASE_PG`: Database name to be used (the application will try to create it if it doesn't exist)

**Example of setting environment variables (for Linux/macOS):**

```bash
export DB_USER_PG="your_username"
export DB_PASSWORD_PG="your_password"
export DB_HOST_PG="localhost"
export DB_PORT_PG="5432"
export DB_DATABASE_PG="amigosecreto_db"
```

**Example of setting environment variables for Windows via Command Prompt or PowerShell:**

```bash
set DB_USER_PG=your_username
set DB_PASSWORD_PG=your_password
set DB_HOST_PG=localhost
set DB_PORT_PG=5432
set DB_DATABASE_PG=amigosecreto_db
```

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/DaviCalo/secret_friend_backend
    ```

2.  **Install Python dependencies:**

    ```bash
    cd .\secret_friend_backend\
    pip install psycopg2
    ```

## How to Run

1.  **Ensure your PostgreSQL server is running.**
2.  **Define environment variables** as per the "Database Configuration" section.
3.  **Execute the main script:**
    ```bash
    python main.py
    ```

The application will start in the console, displaying the main menu for interaction.
