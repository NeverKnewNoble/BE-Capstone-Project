# Task Management System

A user-friendly Task Management System that allows users to create, manage, and track their tasks efficiently. The system offers essential features for managing tasks, including filtering options based on status, priority, and due date.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- User Registration and Authentication
- Create, Retrieve, Update, and Delete Tasks
- Mark Tasks as Complete or Incomplete
- Filter Tasks by Status, Priority, and Due Date
- Intuitive User Interface

# Task Management System

A user-friendly Task Management System that allows users to create, manage, and track their tasks efficiently. The system offers essential features for managing tasks, including filtering options based on status, priority, and due date.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- User Registration and Authentication
- Create, Retrieve, Update, and Delete Tasks
- Mark Tasks as Complete or Incomplete
- Filter Tasks by Status, Priority, and Due Date
- Intuitive User Interface

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: (if applicable, mention frameworks like React, Angular, etc.)
- **Database**: SQLite / PostgreSQL / MySQL (choose one based on your implementation)
- **Version Control**: Git
- **Deployment**: (e.g., Heroku, AWS, etc. if applicable)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NeverKnewNoble/BE-Capstone-Project.git
   cd task-management-system

## Installation Steps

1. **Create a virtual environment:**
   ```bash
   python -m venv venv

## Activate the virtual environment:

- For Windows:
  ```bash
     venv\Scripts\activate
- For macOS/Linux:
  ```bash
    source venv/bin/activate

## Install the required packages:
```pip install -r requirements.txt```

- Run migrations:
  ```bash
  python manage.py migrate

## Start the development server:

  ```python manage.py runserver```

## Usage
  - Register a new user by sending a POST request to /register/.
  - Log in to obtain a JWT token for authentication.
  - Use the API endpoints to manage tasks.
  - API Endpoints
  - User Endpoints
  - POST /register/ - Create a new user.
  - POST /login/ - User login and token generation (JWT).
  - GET /users/<id>/ - Retrieve user details.
  - PUT /users/<id>/ - Update user details.
  - DELETE /users/<id>/ - Delete user account.

## Task Endpoints
  - GET /tasks/ - List all tasks (with optional filters).
  - POST /tasks/ - Create a new task.
  - GET /tasks/<id>/ - Retrieve task details.
  - PUT /tasks/<id>/ - Update task details.
  - DELETE /tasks/<id>/ - Delete a task.
  - POST /tasks/<id>/mark_complete/ - Mark a task as complete.
  - POST /tasks/<id>/mark_incomplete/ - Revert task to incomplete.

## Contributing
Contributions are welcome! Feel free to submit a pull request if you have suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For inquiries or feedback, please contact:

- Email = nortexnoble@gmail.com
GitHub: Nortex
