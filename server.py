import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='horenSmart')

class Fold(BaseModel):
    name: str
    id_user: int


@app.post('get_fold/', response_class=Fold)
async def get_folds():
    pass