from fastapi import FastAPI

app = FastAPI()
user = [
    {'id': 1, 'name': 'User1'},
    {'id': 2, 'name': 'User2'},
    {'id': 3, 'name': 'User3'},
    {'id': 4, 'name': 'User4'}
]


@app.get("/")
async def root():
    return {"message": "This is a simple API using FastAPI. Check /docs for available endpoints."}

@app.get("/users")
async def get_users():
    return user

@app.get("/user/{id}")
async def get_users(id:int):
    return [ out_user for out_user in user if out_user['id'] == id ]
