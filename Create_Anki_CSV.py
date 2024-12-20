import csv  # Imports the `csv` module for working with CSV files.

def create_anki_csv(flashcards_output, filename="anki_flashcards.csv", delimiter=";"):  # Defines a function named `create_anki_csv` that takes three arguments:
                                                                                       # `flashcards_output`: The string containing the flashcard output from the Gemini model.
                                                                                       # `filename`: The name of the CSV file to be created (default: "anki_flashcards.csv").
                                                                                       # `delimiter`: The delimiter to use in the CSV file (default: ",").

    """
    Converts flashcard output to Anki-compatible CSV format.
    """

    field1_lines = []  # Creates an empty list to store the lines containing "Field 1".
    field2_lines = []  # Creates an empty list to store the lines containing "Field 2".
    lines = flashcards_output.splitlines()  # Splits the `flashcards_output` string into a list of lines.
    print(lines)

    for line in lines:  # Starts a loop that iterates through each line in the `lines` list.
        line = line.strip()  # Removes any leading or trailing whitespace from the current line.
        if line.startswith("Field 1:"):  # Checks if the line starts with "Field 1:".
            field1_lines.append(line.split("Field 1:")[1].strip())  # If it does, it splits the line at "Field 1:", takes the second part (the content), removes any leading/trailing whitespace, and appends it to the `field1_lines` list.
        elif line.startswith("Field 2:"):  # Checks if the line starts with "Field 2:".
            field2_lines.append(line.split("Field 2:")[1].strip())  # If it does, it splits the line at "Field 2:", takes the second part (the content), removes any leading/trailing whitespace, and appends it to the `field2_lines` list.

    # Combine the lists into flashcards  # This section combines the `field1_lines` and `field2_lines` lists into a list of flashcards.
    flashcardsList = [[field1, field2] for field1, field2 in zip(field1_lines, field2_lines)]  # Uses a list comprehension to create a new list called `flashcards`. It iterates through the `field1_lines` and `field2_lines` lists simultaneously using `zip`, and for each pair of corresponding elements, it creates a new list `[field1, field2]` and appends it to the `flashcards` list.
    print(flashcardsList)


    with open(filename, "w", encoding="utf-8", newline="") as csvfile:  # Opens the CSV file specified by `filename` in write mode ("w") with UTF-8 encoding and no extra newlines.
        writer = csv.writer(csvfile, delimiter=delimiter)  # Creates a `csv.writer` object to write data to the CSV file using the specified `delimiter`.
        writer.writerows(flashcardsList)  # Writes the `flashcards` list to the CSV file, where each sublist in `flashcards` becomes a row in the CSV.