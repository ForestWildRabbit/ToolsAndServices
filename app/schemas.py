from pydantic import BaseModel, Field
from typing import Optional, Annotated


class UsersLoad(BaseModel):
    number: Annotated[int, Field(ge=1, le=100)]


class LocationStreet(BaseModel):
    number: int
    name: str


class LocationCoordinates(BaseModel):
    latitude: str
    longitude: str


class LocationTimezone(BaseModel):
    offset: str
    description: str


class Location(BaseModel):
    street: LocationStreet
    city: str
    state: str
    country: str
    postcode: str
    coordinates: LocationCoordinates
    timezone: LocationTimezone


class Name(BaseModel):
    title: str
    first: str
    last: str


class Login(BaseModel):
    uuid: str
    username: str
    password: str
    salt: str
    md5: str
    sha1: str
    sha256: str


class Dob(BaseModel):
    date: str
    age: int


class Registered(BaseModel):
    date: str
    age: int


class Id(BaseModel):
    name: str
    value: Optional[str]


class Picture(BaseModel):
    large: str
    medium: str
    thumbnail: str


class User(BaseModel):
    gender: str
    name: Name
    location: Location
    email: str
    login: Login
    dob: Dob
    registered: Registered
    phone: str
    cell: str
    id: Id
    picture: Picture
    nat: str
