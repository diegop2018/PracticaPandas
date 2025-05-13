import pandas as pd
import pyodbc


class DatabaseManager:
    def __init__(self, server, database, user, password):
        self.connection_string = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={user};'
            f'PWD={password}'
        )
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establece la conexión a la base de datos."""
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def execute_stored_procedure(self, stored_procedure):
        """Ejecuta un procedimiento almacenado y devuelve los resultados como un DataFrame."""
        self.cursor.execute(stored_procedure)
        result = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]
        return pd.DataFrame.from_records(result, columns=columns)

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()