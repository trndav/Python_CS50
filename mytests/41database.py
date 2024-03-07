import sqlite3

class Person:
    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect("database.db") # Create or connect to database file
        self.cursor = self.connection.cursor() 
    
    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
                       """.format(id_number))
        results = self.cursor.fetchone()
        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    
    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({}, "{}", "{}", {})
        """.format(self.id_number, self.first, self.last, self.age))

        self.connection.commit()

p1 = Person()
p1.load_person(1)
print(p1.first)
print(p1.last)
print(p1.age)

p2 = Person(6, "Jack", "Russ", 32)
p2.insert_person()
print(p2.first)
print(p2.last)
print(p2.age)

connection = sqlite3.connect("database.db") # Create or connect to database file
cursor = connection.cursor() 

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)
connection.close()

# connection = sqlite3.connect("database.db") # Create or connect to database file
# cursor = connection.cursor() 

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS persons (
#                id INTEGER PRIMARY KEY,
#                first_name TEXT,
#                last_name TEXT,
#                age INTEGER
#     )
# """)

# cursor.execute("""
# INSERT INTO persons VALUES
#             (1, "Paul", "Smith", 24),
#             (2, "Bob", "Trog", 22),
#             (3, "Tim", "Gog", 34)            
# """)

# search = cursor.execute("""
# SELECT * FROM persons
#                WHERE last_name = "Smith"
#                """)
# rows = search.fetchall()
# print(rows)

# connection.commit()
# connection.close()