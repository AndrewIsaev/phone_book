import os.path

from models import Person

FIELDNAMES = [
    "last_name",
    "first_name",
    "middle_name",
    "organization",
    "work_phone",
    "mobile_phone",
]
PHONE_BOOK = os.path.join(".", "phonebook.txt")


def load_data() -> list[Person] | str:
    try:
        with open(PHONE_BOOK, "r") as file:
            lines = file.readlines()
            persons = []
            for line in lines:
                fields = line.strip().split(";")
                person = Person(
                    last_name=fields[0],
                    first_name=fields[1],
                    middle_name=fields[2],
                    organization=fields[3],
                    work_phone=fields[4],
                    mobile_phone=fields[5],
                )
                persons.append(person)
            return persons
    except FileNotFoundError:
        return "File not found"


def save_data(persons: list[Person]) -> None:
    with open(PHONE_BOOK, "w") as file:
        for person in persons:
            line = person.add_person()
            file.write(line)


def display_persons(persons: list[Person]) -> None:
    for person in persons:
        print(person.person_view().strip())


def show_paginate_persons(persons: list[Person]) -> None:
    per_page: int = int(input("Row by page: "))
    all_pages: int = int(len(persons) / per_page) + 1
    print(f"All pages: {all_pages}")
    page: int = int(input("Choose page: "))
    if page > all_pages:
        print("Wrong page! Choose correct page.")
    [
        print(person.person_view().strip())
        for person in persons[(page - 1) * per_page: per_page * page]
    ]


def add_person(persons: list[Person]) -> None:
    new_entry: dict = {}
    for field in FIELDNAMES:
        new_entry[field] = input(f"Enter {field}: ")

    person: Person = Person(**new_entry)
    persons.append(person)
    save_data(persons)
    print("Entry added successfully.")


def edit_person(persons: list[Person], index: int):
    if 0 <= index < len(persons):
        person = persons[index].model_dump()
        for field in FIELDNAMES:
            new_value = input(f"Enter new {field} (current: {person[field]}): ")
            if new_value:
                person[field] = new_value
        person = Person(**person)
        persons[index] = person
        save_data(persons)
        print("Entry edited successfully.")
    else:
        print("Invalid index.")


def search_persons(persons: list[Person], search_terms: str) -> list[Person]:
    search_results: list[Person] = []
    for person in persons:
        if any(
                term.lower() in value.lower()
                for term, value in zip(search_terms, person.model_dump().values())
        ):
            search_results.append(person)
    return search_results
