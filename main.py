from models import Person
from utils import (
    load_data,
    show_paginate_persons,
    add_person,
    edit_person,
    search_persons,
    display_persons,
)


def main():
    persons: list[Person] = load_data()

    while True:
        print("\nPhonebook Menu:")
        print("1. Display persons")
        print("2. Add new person")
        print("3. Edit person")
        print("4. Search persons")
        print("5. Quit")

        choice: str = input("Enter your choice: ")

        match choice:
            case "1":
                show_paginate_persons(persons)
            case "2":
                add_person(persons)
            case "3":
                index: int = int(input("Enter the index of the person to edit: "))
                edit_person(persons, index)
            case "4":
                search_terms: list[str] = input("Enter search terms separated by spaces: ").split()
                search_results: list[Person] = search_persons(persons, search_terms)
                display_persons(search_results)
            case "5":
                break
            case _:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
