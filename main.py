import random


data = []


def generate_id():
    return "".join(random.choices("0123456789", k=6))


def is_valid(val):
    if val is None or val.strip() == "":
        return False
    return True


def find(id_val):
    for i in range(len(data)):
        if data[i] is not None and data[i]["id"] == id_val:
            return i
    return -1


def list_notes():
    if len(data) == 0:
        print("\nNo notes available.")
        return

    print("\nListing all notes:")
    for i in range(len(data)):
        if data[i] is not None:
            print(f"ID: {data[i]['id']} | Note: {data[i]['body']}")


def add_note(note):
    if not is_valid(note):
        print("Invalid note content.")
        return

    note_id = generate_id()
    data.append({"id": note_id, "body": note})
    print(f"Note added successfully! Generated ID: {note_id}")


def edit_note(note_id, edited):
    if not is_valid(note_id):
        print("Invalid ID.")
        return

    if not is_valid(edited):
        print("Invalid edited note.")
        return

    index = find(note_id)

    if index < 0:
        print(f"Note with ID: {note_id} no where to be found lol.")
        return

    data[index]["body"] = edited
    print(f"Note edited successfully. ID: {note_id}")


def delete_note(note_id):
    if not is_valid(note_id):
        print("Invalid ID.")
        return

    index = find(note_id)

    if index < 0:
        print(f"Note with ID: {note_id} could NOT be found.")
        return

    deleted = data.pop(index)
    print(f"Note deleted successfully. ID: {note_id}")
    return deleted


def show_menu():
    print("\n--- Precisious note App ;) ---")
    print("1. List Notes")
    print("2. Add Note")
    print("3. Edit Note")
    print("4. Delete Note")


def main():
    while True:
        show_menu()
        choice = input().strip()

        if choice == "1":
            list_notes()
        elif choice == "2":
            # Auto-generates ID internally, only asking for content
            note = input("Enter Note Content: ")
            add_note(note)
        elif choice == "3":
            note_id = input("Enter Note ID to Edit: ")
            edited = input("Enter New Content: ")
            edit_note(note_id, edited)
        elif choice == "4":
            note_id = input("Enter Note ID to Delete: ")
            delete_note(note_id)
        else:
            print("Invalid option.")


main()