from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers.user import router as user_router

# 1. Create the database tables
# This line tells SQLAlchemy to look at your models (like app/models/user.py)
# and create those tables in your database automatically if they don't exist.
models.Base.metadata.create_all(bind=engine)

# 2. Initialize the FastAPI application
app = FastAPI(
    title="My Social Media API",
    description="A cleanly structured FastAPI application",
    version="1.0.0",
)

# 3. Connect your Routers
# This registers all the endpoints from app/routers/users.py under your app instance.
app.include_router(user_router)


# 4. Create a basic root endpoint just to test if the server is running
@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Welcome to the FastAPI application!"}



