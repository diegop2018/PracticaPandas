#Ejecutar procedimiento almacenado desde python desde una base de datos de MSSQL


from Internals.DatabaseManager import DatabaseManager
from Internals.save_stored_procedure_results_to_csv import save_stored_procedure_results_to_csv

# Uso de la clase DatabaseManager
if __name__ == "__main__":
    # Configuración de la base de datos
    server = 'CRMV-FRONTDDBB\\FRONTIERDB'
    database = 'COMPURENT'
    user = 'informesBi'
    password = 'Compur3nt.May25+'
    stored_procedure = 'COMPURENT.dbo.SP_ConsultasPowerBI @pOpcion = 4'

    # Crear una instancia de DatabaseManager
    db_manager = DatabaseManager(server, database, user, password)

    try:
        # Conectar a la base de datos
        db_manager.connect()

        # Ejecutar el procedimiento almacenado
        df = db_manager.execute_stored_procedure(stored_procedure)
        print(df)  # Mostrar el DataFrame con los resultados

    finally:
        # Cerrar la conexión
        db_manager.close()

save_stored_procedure_results_to_csv(df,'Dataload')

