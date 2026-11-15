"""A small demo REST API created specifically for practicing API testing.

WARNING: This is a learning/demo application, not production authentication.
It stores data in memory, so data resets when the server restarts.
"""
from typing import Optional
from fastapi import FastAPI, Header, HTTPException, status
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title="QA Practice API",
    description="Demo REST API for a Postman + Python + Pytest portfolio project.",
    version="1.0.0",
)

USERS = {
    1: {"id": 1, "name": "Asha Kumar", "email": "asha@example.com"},
    2: {"id": 2, "name": "Ravi Das", "email": "ravi@example.com"},
}
NEXT_ID = 3
DEMO_USERNAME = "demo"
DEMO_PASSWORD = "demo123"
DEMO_TOKEN = "qa-demo-token"


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr


class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr


class UserPatch(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=80)
    email: Optional[EmailStr] = None


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok", "service": "QA Practice API"}


@app.get("/users", tags=["Users"])
def list_users():
    return list(USERS.values())


@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(payload: UserCreate):
    global NEXT_ID
    if any(user["email"].lower() == payload.email.lower() for user in USERS.values()):
        raise HTTPException(status_code=409, detail="Email already exists")
    user = {"id": NEXT_ID, "name": payload.name, "email": str(payload.email)}
    USERS[NEXT_ID] = user
    NEXT_ID += 1
    return user


@app.put("/users/{user_id}", tags=["Users"])
def replace_user(user_id: int, payload: UserUpdate):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    if any(u["email"].lower() == payload.email.lower() and u["id"] != user_id
           for u in USERS.values()):
        raise HTTPException(status_code=409, detail="Email already exists")
    USERS[user_id] = {"id": user_id, "name": payload.name, "email": str(payload.email)}
    return USERS[user_id]


@app.patch("/users/{user_id}", tags=["Users"])
def patch_user(user_id: int, payload: UserPatch):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    changes = payload.model_dump(exclude_unset=True)
    if not changes:
        raise HTTPException(status_code=400, detail="At least one field is required")
    if "email" in changes:
        if any(u["email"].lower() == str(changes["email"]).lower() and u["id"] != user_id
               for u in USERS.values()):
            raise HTTPException(status_code=409, detail="Email already exists")
        changes["email"] = str(changes["email"])
    USERS[user_id].update(changes)
    return USERS[user_id]


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    del USERS[user_id]
    return None


@app.post("/auth/login", tags=["Authentication"])
def login(payload: LoginRequest):
    if payload.username != DEMO_USERNAME or payload.password != DEMO_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": DEMO_TOKEN, "token_type": "bearer"}


@app.get("/protected/profile", tags=["Authentication"])
def protected_profile(authorization: Optional[str] = Header(default=None)):
    if authorization != f"Bearer {DEMO_TOKEN}":
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    return {"user": DEMO_USERNAME, "role": "tester", "message": "Access granted"}
