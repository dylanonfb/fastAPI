import secrets

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from typing import Annotated


app = FastAPI()
user = [
    {'id': 1, 'name': 'User1'},
    {'id': 2, 'name': 'User2'},
    {'id': 3, 'name': 'User3'},
    {'id': 4, 'name': 'User4'}
]

creds={'username':'admin','password':'pass'}


@app.get("/")
async def root():
    return {"message": "This is a simple API using FastAPI. Check /docs for available endpoints."}

@app.get("/users")
async def get_users():
    return user

@app.get("/user/{id}")
async def get_users(id:int):
    return [ out_user for out_user in user if out_user['id'] == id ]


security = HTTPBasic()


def user_prompt(credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    in_user = credentials.username.encode('utf8')
    in_pass = credentials.password.encode('utf8')

    if secrets.compare_digest(in_user,creds['username'].encode('utf8')) \
            and secrets.compare_digest(in_pass,creds['password'].encode('utf8')):
        return in_user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.get("/login")
async def login(user: Annotated[str, Depends(user_prompt)]):
    return {'user':user}