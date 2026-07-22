from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List

class FileResponse(BaseModel):
    id: int
    name: str
    telegram_file_id: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class FolderBase(BaseModel):
    name: str
    parent_id: Optional[int] = None

class FolderCreate(FolderBase):
    author_id: int

class FolderResponse(FolderBase):
    id: int
    author_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FolderDetailResponse(FolderResponse):
    subfolders: List[FolderResponse] = []
    files: List['FileResponse'] = []