import asyncio
from fastapi import FastAPI, Depends

import schemes
from db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(title='horenSmart')


@app.post('/create_folder/', response_model=schemes.FolderResponse)
async def create_folders(folder: schemes.FolderCreate, db: AsyncSession = Depends(get_db)):
    pass