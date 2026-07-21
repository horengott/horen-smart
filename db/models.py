from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    tg_id = Column(BigInteger, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)

    folders = relationship("Folder", back_populates="author")


class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship("User", back_populates="folders")

    parent_id = Column(Integer, ForeignKey("folders.id"), nullable=True)
    subfolders = relationship("Folder", backref="parent_folder", remote_side=[id])

    files = relationship("File", back_populates="folder", cascade="all, delete-orphan")


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    telegram_file_id = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    folder_id = Column(Integer, ForeignKey("folders.id"), nullable=False)
    folder = relationship("Folder", back_populates="files")