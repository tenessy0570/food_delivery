import re

from pydantic import BaseModel, field_validator


class UserCreateOrUpdateSchema(BaseModel):
    login: str
    email: str
    phone_number: str
    is_active: bool = False

    @field_validator("email")
    def validate_email(cls, value):
        # https://stackoverflow.com/a/14075810/17270019
        email_pattern = r"""([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|"([]!#-[^-~ \t]|(\\[\t -~]))+")@[0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?(\.[0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?)+"""
        if not re.match(
            email_pattern,
            value
        ):
            raise ValueError("email field doesn't must match email pattern")

        return value

    @field_validator("login")
    def validate_login(cls, value):
        if not re.match(r"^\w{8,}$", value):
            raise ValueError("login must be at least 8 characters long and not contain special characters")

        return value

    @field_validator("phone_number")
    def validate_phone_number(cls, value):
        if not re.match(r"^\+\d{11}$", value):
            raise ValueError("phone number must be 11 characters long and start with '+'")

        return value
