from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def get_user():
  return {"user":"me"}

@app.get("/users/{user_id}")
async def get_user(user_id):
  return {"user":user_id}