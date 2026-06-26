from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


# Database model - like your Pydantic model but also create a DB Table
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    status: str = "todo"
    description: Optional[str] = None


# SQLite database - stored in a file, no server needed
DATABASE_URL = "sqlite:///tasks.db"
engine = create_engine(DATABASE_URL)


def create_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
