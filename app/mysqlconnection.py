#config/mysql

import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        try:
            connection = pymsql.connect(
                host = 'Localhost',
                port = 3306,
                user = 'root',
                password = 'root',
                database = db,
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor,
                autocommit = True
            )
            self.connection = connection
        except pymysql.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None # Establece la conexion a None en caso de error

        def query_db(self, query,data=None):
            if not self.connection:
                print("No hay conexióna la base de datos")
                return False
            
            with self.connection.cursor() as cursor:
                try:
                    if data:
                        print("Runing query", cursor.mogrify(query, data))
                    cursor.execute(quey, data)
                    if query.lower().find("insert") >=0:
                        self.connection.commit()
                        return cursor.lastrowid
                    elif query.lower().find("Select") >=0:
                        result= cursor.fetchall()
                        return result
                    else:
                        self.connection.commit()#commit para Update / Delete
                        return True # para UPDATE/DELETE
                except Exception as e:
                    print(f" Hubo un problema con la consulta: {e}")
                    return False
                finally:
                    pass #No cerramos la conexion aqui

def connectToMySQL(db):
    return MySQLConnection(db)