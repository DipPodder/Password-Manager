import hashlib

# Initialize an empty dictionary to store passwords
passwords = {}

def hash_password(password):
    """Hashes the password using SHA-256."""
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    return hasher.hexdigest()

def store_password():
    """Store a new password."""
    website = input("Enter the website or service name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Hash the password before storing it
    hashed_password = hash_password(password)
    
    # Store the hashed password in the dictionary
    passwords[website] = {
        'username': username,
        'password': hashed_password
    }
    print(f"Password for {website} has been stored securely.")

def retrieve_password():
    """Retrieve a stored password."""
    website = input("Enter the website or service name: ")

    if website in passwords:
        username = passwords[website]['username']
        print(f"Username: {username}")
        print("Password: **** (Password hashing prevents retrieval)")
    else:
        print(f"No password found for {website}.")

def main():
    while True:
        print("\nPassword Manager Menu:")
        print("1. Store a new password")
        print("2. Retrieve a stored password")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            store_password()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty dictionary to store passwords
passwords = {}

# Your hash_password, store_password, and retrieve_password functions go here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_password', methods=['POST'])
def store_password_route():
    if request.method == 'POST':
        website = request.form['website']
        username = request.form['username']
        password = request.form['password']

        # Hash the password before storing it
        hashed_password = hash_password(password)

        # Store the hashed password in the dictionary
        passwords[website] = {
            'username': username,
            'password': hashed_password
        }
        return render_template('index.html', message=f"Password for {website} has been stored securely.")

@app.route('/retrieve_password', methods=['POST'])
def retrieve_password_route():
    if request.method == 'POST':
        website = request.form['retrieve-website']

        if website in passwords:
            username = passwords[website]['username']
            return render_template('password.html', username=username)
        else:
            return render_template('password.html', error=f"No password found for {website}.")

if __name__ == '__main__':
    app.run(debug=True)
