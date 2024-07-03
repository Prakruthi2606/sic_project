import pymysql

# connect to MySQL
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="prakruthi@2606",
    database="prakruthi"
)

mycursor = mydb.cursor()

# function to add a user
def add_user(id, name, password, email, date, transaction_id, transaction_type, account_balance):
    sql = "INSERT INTO users (id, name, password, email, date, transaction_id, transaction_type, account_balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id, name, password, email, date, transaction_id, transaction_type, account_balance)
    mycursor.execute(sql, val)
    mydb.commit()
    print("User added successfully.") 

# function to delete user by id
def delete_user(id):
    sql = "DELETE FROM users WHERE id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()
    print("User with id:{} deleted".format(id))

# function to update user details
def update_user(id, name, password, email, date, transaction_id, transaction_type, account_balance):
    sql = "UPDATE users SET name = %s, password = %s, email = %s, date = %s, transaction_id = %s, transaction_type = %s, account_balance = %s WHERE id = %s"
    val = (name, password, email, date, transaction_id, transaction_type, account_balance, id)
    mycursor.execute(sql,val)
    mydb.commit()
    print("User details updated successfully.")

# search user based on id entered
def search_user_id(id):
    sql = "SELECT * FROM users WHERE id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    if result:
        print("User found")
        print("{:<5} {:<20} {:<20} {:<25} {:<20} {:<20} {:<20} {:<20}".format("ID", "Name", "Password", "Email", "Date", "transaction_id", "transaction_type", "account_balance"))
        print("-" * 170)
        print("{:<5} {:<20} {:<20} {:<25} {:<20} {:<20} {:<20} {:<20}".format(result[0],result[1],result[2],result[3],result[4].isoformat(),result[5],result[6],result[7]))
    else:
        print("No users found.")

# function to display all users
def display_users():
    mycursor.execute("SELECT * FROM users")
    result = mycursor.fetchall()
    if result:
        print("{:<5} {:<20} {:<20} {:<25} {:<20} {:<20} {:<20} {:<20}".format("ID", "Name", "Password", "Email", "Date", "transaction_id", "transaction_type", "account_balance"))
        print("-" * 170)
        for user in result:
            print("{:<5} {:<20} {:<20} {:<25} {:<20} {:<20} {:<20} {:<20}".format(user[0], user[1], user[2], user[3], user[4].isoformat(), user[5], user[6], user[7]))
    else:
        print("User not found.")

# Main function
def main():
    while True:
        print("\n1. Add one user")
        print("2. Delete one user")
        print("3. Update user details")
        print("4. Search one user")
        print("5. Display all users")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            password = input("Enter user password: ")
            email = input("Enter user e-mail: ")
            date = input("Enter date(YYYY-MM-DD) of transaction: ") 
            transaction_id = int(input("Enter transaction ID: "))
            transaction_type = input("Enter transaction type(deposit or withdrawl): ")
            account_balance = input("Enter account balance: ")
            add_user(id, name, password, email, date, transaction_id, transaction_type, account_balance)
        
        elif choice == '2':
            id = input("Enter user id to be deleted: ")
            delete_user(id)

        elif choice == '3':
            id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            password = input("Enter user password: ")
            email = input("Enter user e-mail: ")
            date = input("Enter date(YYYY-MM-DD) of transaction: ") 
            transaction_id = int(input("Enter transaction ID: "))
            transaction_type = input("Enter transaction type(deposit or withdrawl): ")
            account_balance = input("Enter account balance: ")
            update_user(id, name, password, email, date, transaction_id, transaction_type, account_balance)

        elif choice == '4':
            id = input("Enter user id to search that user: ")
            search_user_id(id)
        
        elif choice == '5':
            display_users()
        
        elif choice == '6':
            print("Exiting program.")
            break; 
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()