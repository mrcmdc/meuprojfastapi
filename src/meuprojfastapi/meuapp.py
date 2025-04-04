from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from meuprojfastapi.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

meuapp = FastAPI()

database = []


@meuapp.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World of FastAPI'}


@meuapp.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@meuapp.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@meuapp.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'User {user_id} not found',
        )

    user_index = user_id - 1
    database[user_index] = UserDB(id=user_id, **user.model_dump())
    return database[user_index]


@meuapp.delete('/users/{user_id}', response_model=UserPublic)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'User {user_id} not found',
        )

    user_index = user_id - 1
    deleted_user = database.pop(user_index)
    return deleted_user
