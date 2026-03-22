from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    login: str
    password: str
    email: EmailStr

    @property
    def is_valid_login(self):
        if len(self.login) < 5 or len(self.login) > 30:
            return False

        login_without_underscore = self.login.replace("_", "")
        if not login_without_underscore.isalnum():
            return False

        return True

    @property
    def is_valid_password(self):
        if len(self.password) < 8 or len(self.password) > 30:
            return False

        if not any(char.isupper() for char in self.password):
            return False

        if not any(char.islower() for char in self.password):
            return False

        if not any(char.isdigit() for char in self.password):
            return False

        return True


class UserLogin(BaseModel):
    login: str
    password: str
