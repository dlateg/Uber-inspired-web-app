from typing import Optional
from cars import initial_db_state
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Driver(SQLModel, table=True):
    vehicle_id: str = Field(default=None, primary_key=True, nullable=False)
    latitude: float
    longitude: float
    place: Optional[str] = Field(default=None, nullable=False)


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


def transform(driver_list):
    formatted_data = []
    for item in driver_list:
        formatted_data.append(
            {
                "vehicle_id": item.vehicle_id,
                "latitude": item.latitude,
                "longitude": item.longitude,
                "place": item.place,
            }
        )
    return formatted_data


def get_drivers():
    with Session(engine) as sess:
        statement = select(Driver)
        results = sess.exec(statement).all()
        return transform(results)


def main():
    create_db_and_tables()
    create_drivers()
    get_drivers()


if __name__ == "__main__":
    main()
