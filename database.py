import json
from typing import Optional
from cars import initial_db_state
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Driver(SQLModel, table=True):
    vehicle_id: str = Field(default=None, primary_key=True, nullable=False)
    latitude: float
    longitude: float
    place: Optional[str] = Field(default=None, nullable=False)

    #convert object to dict representantion
    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "place": self.place,
        }


sqlite_file_name = "drivers.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_drivers():
    with Session(engine) as sess:
        #check if item exists before adding it
        for item in initial_db_state["drivers_location"]:
            existing_driver = sess.exec(select(Driver).where(Driver.vehicle_id == item["vehicle_id"])).first()
            if not existing_driver:
                sess.add(Driver(**item))
        sess.commit()


def transform(driver_list):
    formatted_data = []
    for item in driver_list:
        formatted_data.append(item.to_dict())
    return formatted_data


def get_drivers():
    with Session(engine) as sess:
        statement = select(Driver)
        results = sess.exec(statement).all()  
        tranformed_results = transform(results)
        return json.dumps(tranformed_results)

print (get_drivers())

def main():
    create_db_and_tables()
    create_drivers()
    get_drivers()


if __name__ == "__main__":
    main()
