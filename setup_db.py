import MySQLdb

try:
    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        password='Ashish@9630'
    )
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS leave_management")
    cursor.execute("USE leave_management")
    
    with open('schema.sql', 'r') as f:
        sql_commands = f.read().split(';')
        for command in sql_commands:
            if command.strip():
                try:
                    cursor.execute(command)
                except Exception as e:
                    print(f"Error: {e}")
    
    conn.commit()
    print("Database setup successful!")
    
except Exception as e:
    print(f"Error connecting to MySQL: {e}")
    print("Please update MYSQL_PASSWORD in config.py with your MySQL root password")
finally:
    if 'conn' in locals():
        conn.close()
