# Open the file and read its contents
with open("books.txt") as book_file:
    # Iterate through each line in the file
    for line in book_file:
        # Remove any leading or trailing whitespace (including newline characters)
        clean_line = line.strip()
        # Display the cleaned line only if it's not empty
        if clean_line:
            print(clean_line)

input("\nPressione Enter para sair...")
