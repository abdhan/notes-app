# Simple Notes Program - Version 2

print("=== MY NOTES ===")
print("1. Write note")
print("2. Read notes")

choice = input("Choose (1 or 2): ")

if choice == "1":
    # Write a note to file
    note = input("Write your note: ")

    with open("my_notes.txt", "w") as file:
        file.write(note)

    print("Note saved!")

elif choice == "2":
    # Read notes from file
    try:
        with open("my_notes.txt", "r") as file:
            content = file.read()
        print(f"\nYour note: {content}")
    except FileNotFoundError:
        print("No notes found yet!")