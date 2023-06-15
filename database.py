from typing import Optional
from cars import initial_db_state
from sqlmodel import Field, Session, SQLModel, create_engine


class Driver(SQLModel, table=True):
    vehicle_id: str = Field(primary_key=True)
    latitude: float
    longitude: float
    place: Optional[str] = None


sqlite_file_name = "drivers.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_drivers():
    with Session(engine) as sess:
        for item in initial_db_state["drivers_location"]:
            sess.add(Driver(**item))
        sess.commit()


if __name__ == "__main__":
    create_db_and_tables()
    create_drivers()
