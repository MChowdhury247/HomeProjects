import csv  # Module used for reading and writing CSV files.

def read_csv(filename):
    """
    Read and print rows from a CSV file.

    Args:
        filename (str): The name of the CSV file to read.
    """
    with open(filename, 'r', newline='') as file:
        """
        Open the CSV file in read mode ('r').
        The 'newline' parameter ensures universal newline support.
        """
        csv_reader = csv.reader(file)  # Create a CSV reader object.
        next(csv_reader)  # Skip the first line (header).
        for row in csv_reader:  # Iterate over each row in the CSV file.
            print(', '.join(row))  # Join each row's words with a comma and print.

if __name__ == "__main__":
    """
    If this script is run directly (not imported as a module),
    execute the code below.
    """
    csv_filename = "names.csv"  # Name of the CSV file.
    read_csv(csv_filename)  # Call the function to read the CSV file.
