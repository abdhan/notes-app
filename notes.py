# Simple Notes Program

print("=== MY NOTES ===")

# Write a note to file
note = input("Write your note: ")

with open("my_notes.txt", "w") as file:
    file.write(note)

print("Note saved to my_notes.txt!")