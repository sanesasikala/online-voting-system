import mysql.connector

# Establish database connection
cnx = mysql.connector.connect(
    user='username',
    password='password',
    host='127.0.0.1',
    database='database_name'
)

# Create cursor object
cursor = cnx.cursor()

# Function to get Aadhar details
def get_aadhar_details(aadhar_number):
    query = "SELECT * FROM aadhar_details WHERE id = %s"
    cursor.execute(query, (aadhar_number,))
    result = cursor.fetchone()
    return result

# Function to check if the user has voted
def check_voting_history(aadhar_number):
    query = "SELECT * FROM voting_history WHERE aadhar_number = %s"
    cursor.execute(query, (aadhar_number,))
    result = cursor.fetchone()
    return result

# Function to cast a vote
def cast_vote(aadhar_number, party_name):
    query = "INSERT INTO voting_history (aadhar_number, party_name) VALUES (%s, %s)"
    cursor.execute(query, (aadhar_number, party_name))
    cnx.commit()

# Main program logic
def main():
    aadhar_number = int(input("Enter your Aadhar number: "))
    
    # Get Aadhar details
    details = get_aadhar_details(aadhar_number)
    
    if details:
        print("Aadhar Details:")
        print(f"Name: {details[1]}")
        print(f"Address: {details[2]}")
        print(f"Phone: {details[3]}")
        
        # Check voting history
        history = check_voting_history(aadhar_number)
        
        if history:
            print("You have already voted.")
        else:
            # Display parties
            parties = ["BJP", "Congress", "AAP"]
            print("Available Parties:")
            for i, party in enumerate(parties):
                print(f"{i+1}. {party}")
            
            # Cast vote
            choice = int(input("Enter your choice (1/2/3): "))
            if 1 <= choice <= len(parties):
                party_name = parties[choice - 1]
                cast_vote(aadhar_number, party_name)
                print("Your vote has been cast successfully.")
            else:
                print("Invalid choice.")
    else:
        print("Aadhar number not found.")

# Run the program
if __name__ == "__main__":
    main()

# Close cursor and database connection
cursor.close()
cnx.close()
