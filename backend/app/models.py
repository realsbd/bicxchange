import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel


# Shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    username: str | None = Field(default=None, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    phone_number: str | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None, max_length=255)
    date_of_birth: str | None = Field(default=None, max_length=255)
    avatar: str | None = Field(default=None, max_length=255)
    level: str | None = Field(default=None, max_length=255)
    cgpa: str | None = Field(default=None, max_length=255)
    matric_number: str | None = Field(default=None, max_length=255)
    institution: str | None = Field(default=None, max_length=255)
    faculty: str | None = Field(default=None, max_length=255)
    department: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    username: str | None = Field(default=None, max_length=255)
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    phone_number: str | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None, max_length=255)
    date_of_birth: str | None = Field(default=None, max_length=255)
    avatar: str | None = Field(default=None, max_length=255)
    level: str | None = Field(default=None, max_length=255)
    cgpa: str | None = Field(default=None, max_length=255)
    matric_number: str | None = Field(default=None, max_length=255)
    institution: str | None = Field(default=None, max_length=255)
    faculty: str | None = Field(default=None, max_length=255)
    department: str | None = Field(default=None, max_length=255)


# Properties to receive via API on update, all are optional
class UserUpdate(UserBase):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    username: str | None = Field(default=None, max_length=255)
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    phone_number: str | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None, max_length=255)
    date_of_birth: str | None = Field(default=None, max_length=255)
    avatar: str | None = Field(default=None, max_length=255)
    level: str | None = Field(default=None, max_length=255)
    cgpa: str | None = Field(default=None, max_length=255)
    matric_number: str | None = Field(default=None, max_length=255)
    institution: str | None = Field(default=None, max_length=255)
    faculty: str | None = Field(default=None, max_length=255)
    department: str | None = Field(default=None, max_length=255)


class UserUpdateMe(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    username: str | None = Field(default=None, max_length=255)
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    phone_number: str | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None, max_length=255)
    date_of_birth: str | None = Field(default=None, max_length=255)
    avatar: str | None = Field(default=None, max_length=255)
    level: str | None = Field(default=None, max_length=255)
    cgpa: str | None = Field(default=None, max_length=255)
    matric_number: str | None = Field(default=None, max_length=255)
    institution: str | None = Field(default=None, max_length=255)
    faculty: str | None = Field(default=None, max_length=255)
    department: str | None = Field(default=None, max_length=255)


class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    items: list["Item"] = Relationship(back_populates="owner")


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: uuid.UUID


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int


# Shared properties
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str = Field(min_length=1, max_length=255)


# Properties to receive on item update
class ItemUpdate(ItemBase):
    title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


# Database model, database table inferred from class name
class Item(ItemBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False
    )
    owner: User | None = Relationship(back_populates="items")


# Properties to return via API, id is always required
class ItemPublic(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int


# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str = Field(min_length=8, max_length=40)

# Community chat
class CommunityBase(SQLModel):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    image: str | None = Field(default=None, max_length=255)

class CommunityCreate(CommunityBase):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    image: str | None = Field(default=None, max_length=255)

class CommunityUpdate(CommunityBase):
    name: str | None = Field(max_length=255)
    description: str | None = Field(max_length=255)
    image: str | None = Field(max_length=255)

class Community(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

class CommunityPublic(CommunityBase):
    id: int

class CommunitiesPublic(SQLModel):
    data: list[CommunityPublic]
    count: int
