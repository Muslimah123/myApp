from pickle import APPEND
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydatabase",
)

# Create a cursor object
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
''')

# Create the products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL UNIQUE,
        price FLOAT NOT NULL
    )
''')

# Create the voice_transcripts table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS voice_transcripts (
        id INT PRIMARY KEY AUTO_INCREMENT,
        users_id INT,
        transcription TEXT NOT NULL,
        confidence_level float DEFAULT NULL,
        date_created DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (users_id) REFERENCES users(id)
    )
''')


# Create the income_statement table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS income_statement (
        id INT PRIMARY KEY AUTO_INCREMENT,
        users_id INT,
        item_name TEXT,
        amount decimal(10,2),
        transaction_type TEXT,
        date_created DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (users_id) REFERENCES users(id)
    )
''')


# Commit the changes
conn.commit()
print(conn)
# def store_voice_transcript(user_id, transcript):
#     with APPEND.app_context():
#         # Connect to the database
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             database="mydatabase",
#         )

#         # Create a cursor object
#         cursor = conn.cursor()

#     # Execute the SQL query to store the voice transcript
#     sql = "INSERT INTO voice_transcripts (user_id, transcript) VALUES (%s, %s)"
#     val = (user_id, transcript)
#     cursor.execute(sql, val)

#     # Commit the changes
#     conn.commit()

#     # Close the connection
#     conn.close()
