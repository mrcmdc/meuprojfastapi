from fastapi import FastAPI

meuapp = FastAPI()


@meuapp.get('/')
def read_root():
    return {'message': 'Hello World of FastAPI'}
