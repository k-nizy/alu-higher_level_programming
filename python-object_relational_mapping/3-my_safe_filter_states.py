#!/usr/bin/python3
"""
Script to safely filter states by name, protected against SQL injection
"""

import MySQLdb
import sys


def safe_filter_states(username, password, dbname, state_name):
    """
    Connects to MySQL database and safely filters states by name
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query with parameterized input
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 5:
        safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
