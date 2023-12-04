import csv
import os

# Path to the CSV file where passwords are stored
csv_file = 'passwords.csv'

def add_password(website: str, username: str, password: str) -> bool:
    """
    Adds a new password entry to the CSV file.

    Args:
        website (str): The website for the password.
        username (str): The username for the password.
        password (str): The password.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([website, username, password])
        return True
    except Exception as e:
        print(f"An error occurred while adding password: {e}")
        return False

def get_password(website: str) -> tuple:
    """
    Retrieves a password for a given website.

    Args:
        website (str): The website to retrieve the password for.

    Returns:
        tuple: A tuple containing username and password if found, (None, None) otherwise.
    """
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == website:
                    return row[1], row[2]
    except Exception as e:
        print(f"An error occurred while retrieving password: {e}")
    return None, None

def delete_password(website: str) -> bool:
    """
    Deletes a password entry for a given website.

    Args:
        website (str): The website for which to delete the password.

    Returns:
        bool: True if the operation was successful and the password was found and deleted, False otherwise.
    """
    lines = []
    found = False
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != website:
                    lines.append(row)
                else:
                    found = True
        if found:
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
            return True
    except Exception as e:
        print(f"An error occurred while deleting password: {e}")
    return False

# Check if the CSV file exists, if not, create it
if not os.path.exists(csv_file):
    try:
        open(csv_file, 'a').close()
    except Exception as e:
        print(f"An error occurred while creating the CSV file: {e}")
