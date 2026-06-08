"""
Ejercicio 2: Patrón Creacional - Factory Method
"""
from abc import ABC, abstractmethod

class DBConnection(ABC):
    """Define la interfaz de lo que creará la fábrica."""
    @abstractmethod
    def connect(self) -> str:
        pass

class SQLServerConnection(DBConnection):
    """Conexión específica a SQL Server."""
    def connect(self) -> str:
        return "Conexión exitosa a SQL Server en puerto 1433."

class PostgreSQLConnection(DBConnection):
    """Conexión específica a PostgreSQL."""
    def connect(self) -> str:
        return "Conexión exitosa a PostgreSQL en puerto 5432."


class ConnectionFactory(ABC):
    """Declara el método fábrica."""
    @abstractmethod
    def create_connection(self) -> DBConnection:
        pass

class SQLServerFactory(ConnectionFactory):
    """Sabe cómo instanciar la conexión de SQL Server."""
    def create_connection(self) -> DBConnection:
        return SQLServerConnection()

class PostgreSQLFactory(ConnectionFactory):
    """Sabe cómo instanciar la conexión de PostgreSQL."""
    def create_connection(self) -> DBConnection:
        return PostgreSQLConnection()


# --- Ejemplo Concreto de Uso ---
if __name__ == "__main__":
    print("=== TEST PATRÓN FACTORY ===")
    
    # Supongamos que el entorno define qué base de datos usar sin que el 
    # código principal de la aplicación tenga que hardcodear los "import" o constructores
    def ejecutar_bussines_logic(fabrica: ConnectionFactory):
        # La aplicación pide una conexión a la fábrica, no sabe qué base de datos es exactamente
        conexion = fabrica.create_connection()
        print(f"Operando con : {conexion.connect()}")

    print("Configurando la aplicación:")
    ejecutar_bussines_logic(SQLServerFactory())
    
    print("\nCambiando el origen de datos:")
    ejecutar_bussines_logic(PostgreSQLFactory())