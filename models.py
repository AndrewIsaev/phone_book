from pydantic import BaseModel, Field


class Person(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    organization: str
    work_phone: str
    mobile_phone: str

    def add_person(self) -> str:
        return (f"{self.last_name};{self.first_name};{self.middle_name};"
                f"{self.organization};{self.work_phone};{self.mobile_phone}\n")

    def person_view(self) -> str:
        return (f"{self.last_name} {self.first_name} {self.middle_name}"
                f" {self.organization} {self.work_phone} {self.mobile_phone}\n")
