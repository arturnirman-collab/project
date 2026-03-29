from pydantic import BaseModel, EmailStr, field_validator
import re

class UserRegister(BaseModel):
    login: str
    password: str
    email: EmailStr

    @field_validator('login')
    def is_valid_login(cls, value: str):
        if len(value) < 5 or len(value) > 30:
            raise ValueError('login must be between 5 and 30 characters long.')

        login_without_underscore = value.replace("_", "")
        if not login_without_underscore.isalnum():
            raise ValueError('login must be alphanumeric or underscore.')

        return value

    @field_validator('password')
    def is_valid_password(cls, value: str):
        if len(value) < 8 or len(value) > 30:
            raise ValueError('password must be between 8 and 30 characters long.')

        if not re.search('[a-z]', value):
            raise ValueError('password must contain at least one lowercase letter.')

        if not re.search('[A-Z]', value):
            raise ValueError('password must contain at least one uppercase letter.')

        if not re.search('[0-9]', value):
            raise ValueError('password must contain at least one digit.')

        if not re.search('\.,<>_\?!@#\$%\^&\*\(\)', value):
            raise ValueError('password must contain at least one special character.')

        return True