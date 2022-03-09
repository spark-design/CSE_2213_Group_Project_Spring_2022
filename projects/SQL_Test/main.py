# Module Imports
import mariadb
import sys

# Connect to MriaDB Platform
try:
    conn = mariadb.connect(
        user = "root",
        password = "",
        host = "127.0.0.1",
        port = 3306,
        database = "cse_2213"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Execute Query
cur.execute(
    "SELECT * FROM books"
)

# Print Result-set
for (ISBN, Title, Author, Year, Genre) in cur:
    print(f"ISBN: {Title}, Title: {Title}, Author: {Author}, Year: {Year}, Genre: {Genre}")

# Close Connection
conn.close()# CSE_2213_Group_Project_Spring_2022
