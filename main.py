# Rui Xu
# Purpose: for Pet Chooser assignment

# Import the MySQL Connector Python library to connect pycham to MySQL database
import mysql.connector
# Import the configuration settings
from configure import config
# Import the Pets class
from pet_class import Pets

# Function to connect to the MySQL database
def connect_to_database():
    try:
        # Establish a database connection using the provided configuration
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as e:  # Handle any connection errors
        print(f"Error connecting to the database: {e}")


# Function to retrieve data from the database and create Pets objects
def retrieve_pet_info(connection):
    cursor = connection.cursor()
    try:
        # SQL query to retrieve pet information from multiple tables
        query = """
        SELECT 
            pets.id, 
            pets.name, 
            pets.age, 
            types.animal_type,
            owners.name
        FROM pets
        JOIN types ON pets.animal_type_id = types.id
        JOIN owners ON pets.owner_id = owners.id;
        """
        cursor.execute(query)  # Execute the SQL query
        pet_info_data = cursor.fetchall()   # Fetch the query results as pet_info_data

        pets_list = []   # Create a list to store Pets objects
        for row in pet_info_data:
            pet = Pets(*row)  # Create a Pets object from each row of data
            pets_list.append(pet)   # Add the Pets object to the list

        return pets_list  # Return the list of Pets objects

    except mysql.connector.Error as e:  # Handle any query execution errors
        print(f"Error retrieving pet information: {e}")

    finally:
        cursor.close()  # Close the cursor no matter an exception is raised or not

# Define a list of pet names and allow the user to choose a pet
def display_pet_list(pets_list):
    print("Please input a number to choose a pet from the list below:")
    for i, pet in enumerate(pets_list):  # Keep track of both the item's index and its value
        print(f"[{i + 1}] {pet.pet_name}")  # Display each pet's name with a number (start from 1)
    print("[Q] Quit")  # Option to quit the program

# Main function to start choose!
def main():
    connection = connect_to_database()
    pet_info_data = retrieve_pet_info(connection)  # Retrieve the updated pet information
    # Start an infinite loop for user interaction
    while True:
        display_pet_list(pet_info_data)   # Display the list of pet names
        choice = input("Choice: ")  # Prompt the user for their choice

        if choice.lower() == "q":
            break                # Exit the loop and end the program when the user wants to quit
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(pet_info_data):
                pet = pet_info_data[choice - 1]   # Subtract 1 from the user's choice to match the true index
                                                  # Get the selected pet object
                # Print the information for the selected pet
                print(f"You have chosen {pet.pet_name}, the {pet.pet_type}. {pet.pet_name} is {pet.pet_age} years old. {pet.pet_name}'s owner is {pet.owner_name}.")
                input("Press [ENTER] to continue.")
            else:
                print("Invalid choice. Please choose a valid option.")
        else:
            print("Invalid choice. Please choose a valid option.")

    # Close the database connection when the program ends
    connection.close()

    # Call the main function
try:
    main()  # Call the main function if the script is executed as the main program
except ValueError as ve:
    print(f"ValueError: {ve}")
except EOFError as ee:
    print(f"EOFError: {ee}")
