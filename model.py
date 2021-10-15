from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
import os


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    author: str
    name: str = Field(sa_column_kwargs={"unique": True})
    secret_name: str
    age: Optional[int] = None


engine = create_engine(os.getenv("DATABASE_URL", ""))
SQLModel.metadata.create_all(engine)
