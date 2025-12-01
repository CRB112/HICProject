import secrets
import psycopg2

def get_connection():
<<<<<<< HEAD
    return psycopg2.connect(database="HIC_db2", user="postgres",
                        password="359846Cb", host="localhost")
=======
    return psycopg2.connect(database="test_db", user="postgres",
                        password="new_password", host="localhost", port="5432")
>>>>>>> 2c1ac99ff6d0038deb7cf974f5bfb0bba6c12328
# !!ADD THIS FILE TO GIT IGNORE ONCE WE START USING DATABASE!!

#This is where well do database connections
