import sqlite3


class databoase:
    def __init__(self):
            self.conn = None
            self.cursor = None



    def connect(self):
            self.conn = sqlite3.connect('mydb.db')
            self.cursor = self.conn.cursor()




    def create_user_table(self):
            self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Telegramusers(
                    id INTEGER RRIMARY KEY,
                    first_name VARCHAR(30),
                    user_id INTEGER UNIQUE,
                    phone_number VARCHAR(50)
                    )

        """ )    

            self.conn.commit()




    def create_categories_table(self):
           self.cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRYMARY KEY,
                name VARVHAR(50)
                )
        """)               

           self.conn.commit()    



    def create_products_table(self):
           self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRYMARY KEY,
                name VARCHAR(100),
                description TEXT,
                price INTEGER,
                photo TEXT,
                category_name VARCHAR(50),
                FOREIGN KEY (category_name) REFERENCES categories(name)
                )
           """)  
           self.conn.commit()



    def create_cart_table(self):
           self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS crat(
                id INTEGER  PRYMARY KEY,
                user INTEFER UNIQUE,
                product INTEGER,
                FOREIGN KEY (user) REFERENCES Telegramusers(user_id)
                FOREIGN KEY (product)  REFERENCES products(id)

                )
           """)
        
           self.conn.commit()
    def add_user(self, first_name, user_id, phone_number):
           self.cursor.execute("""
                INSERT INTO Telegramusers(first_name, user_id,phone_number)
                VALUES (?,?,?)
           """, (first_name,user_id,phone_number))
           self.conn.commit()




    def check_user(self, user_id):
           self.cursor.execute("SELECT user_id FROM Telegramusers WHERE user_id = ?",(user_id,))
           resault = self.cursor.fetchone()
           if resault is not None:
                  return True
           else:
                  return False       

    def close (self):
           self.conn.close()









