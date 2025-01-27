import psycopg2

class Connection:
    HOST     = "your-host"
    USER     = "your-user"
    PASSWORD = "your-password"
    DATABASE = "your-database"
    PORT     = "yoyr-port"
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname   = self.DATABASE,
                user     = self.USER,
                password = self.PASSWORD,
                host     = self.HOST,
                port     = self.PORT
            )
            
            self.cursor = self.conn.cursor()
            print("DB success connection")
        except Exception as e:
            print(f"DB error connection: {e}")
            
    def disconnect(self):
        try:
            self.cursor.close()
            self.conn.close()
            print("DB success disconnect")
        except Exception as e:
            print(f"DB error disconnect: {e}")
            
class Crud(Connection):
    def __init__(self, name: str, last_name: str, age: int):
        self.name      = name
        self.last_name = last_name
        self.age       = age
        
    def create(self):
        try:
            sql = "INSERT INTO person (name, last_name, age) VALUES (%s, %s, %s)"
            params = (self.name, self.last_name, self.age)
            self.connect()
            self.cursor.execute(sql, params)
            self.conn.commit()
            print("DB success create")
            self.disconnect()
            
        except Exception as e:
            print(f"DB error create record: {e}")
            
    def show(self):
        try:
            sql = "SELECT id, name, last_name, age FROM person"
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, LastName: {row[2]}, Age: {row[3]}")
            self.disconnect()

        except Exception as e:
            print(f"DB error show records: {e}")
            
    def update(self, id, new_name, new_last_name, new_age):
        try:
            sql = "UPDATE person SET name = %s, last_name = %s, age = %s WHERE id = %s"
            params = (new_name, new_last_name, new_age, id)
            self.connect()
            self.cursor.execute(sql, params)
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("DB success update.")
            else:
                print("DB record not found.")
            self.disconnect()
        except Exception as e:
            print(f"DB error update record: {e}")
            
    def delete(self, id):
        try:
            sql = "DELETE FROM person WHERE id = %s"
            params = (id)
            self.connect()
            self.cursor.execute(sql, params)
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("DB success delete.")
            else:
                print("DB record not found.")
            self.disconnect()
       
        except Exception as e:
            print(f"DB error delete record: {e}")
            
crud = Crud('Poll', 'CT', 30)
crud.create()
crud.show()
crud.update(1, 'ABC', '123', 25)
crud.show()
crud.delete(1)
