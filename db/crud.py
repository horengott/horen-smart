from sqlalchemy.ext.asyncio import AsyncSession
import models
import schemes


async def create_folder(db: AsyncSession, folder: schemes.FolderCreate):
    new_folder = models.Folder(
        name = folder.name,
        author_id = folder.author_id,
        parent_id = folder.parent_id
    )

    db.add(new_folder)
    db.commit()
    db.refresh()

    return new_folder