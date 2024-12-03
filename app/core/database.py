from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session

sqlite_name = "database.db"
database_url = f"sqlite:///{sqlite_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(database_url, connect_args=connect_args)

# connecting database
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
