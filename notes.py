# Simple Notes Program - Version 4

# Read config
with open("config.txt", "r") as file:
    config = file.read()
    # Extract filename (simple parsing)
    notes_file = config.split("\n")[0].split("=")[1]

print("=== MY NOTES ===")
print("1. Add note")
print("2. Read all notes")

choice = input("Choose (1 or 2): ")

if choice == "1":
    note = input("Write your note: ")
    with open(notes_file, "a") as file:
        file.write(note + "\n")
    print("Note added!")

elif choice == "2":
    try:
        with open(notes_file, "r") as file:
            notes = file.read()
        print(f"\nAll notes:\n{notes}")
    except FileNotFoundError:
        print("No notes found yet!")