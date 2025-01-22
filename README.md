# python-fastapi

Project Folder Structure


api/
│
├── configuration/  # Configuration settings and environment management
│   └── database.py  # Database connection setup
│
├── controllers/ # Bridges HTTP requests with services
│   └── user_controller.py  # Handles request logic for users
│
├── middlewares/ # Global request and response processing
│   └── auth_middleware.py  # (Optional) Middleware for authentication
│
├── models/ # Database table definitions
│   └── user_model.py  # Pydantic models for request/response validation
│
├── repositories/  # Handles database interactions
│   └── user_repository.py  # Handles database queries for users
│
├── routes/ 
│   └── user_routes.py  # API routes for user endpoints
│
├── services/ # Encapsulates business logic
│   └── user_service.py  # Business logic for users
│
├── utils/ # Shared utility functions
│   └── hashing.py  # Utility for password hashing, etc.
│
└── main.py  # FastAPI app entry point