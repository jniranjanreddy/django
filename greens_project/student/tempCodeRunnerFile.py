
from django.db import connection
try:
    connection.ensure_connection()
    print("Connection to MySQL is successful")
except Exception as e:
    print(f"Connection failed: {e}")