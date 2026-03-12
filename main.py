from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from starlette import status


class User(BaseModel):
    username: str
    password: str

    @property
    def is_valid_password(self):
        if len(self.password) < 8:
            return False
        if not any(char.isupper() for char in self.password):
            return False
        if not any(char.islower() for char in self.password):
            return False
        if not any(char.isdigit() for char in self.password):
            return False
        return True

app = FastAPI()

@app.get("/")
async def root():
    with open("README.md", "r", encoding='utf8') as readme:
        readme_content = readme.read()

    return {"info about the project": readme_content}

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: User):
    # TODO: Implement user registration logic here
    if not user.is_valid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password does not meet complexity requirements.")
    if user.username in ["existing_user1", "existing_user2"]:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    # TODO: Save the user to the database (not implemented in this example)
    return {"message": f"User {user.username} registered successfully!"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()