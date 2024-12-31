from sqlalchemy import create_engine

def create_db_engine(db_url):
    """Crea un motor de conexión a la base de datos."""
    return create_engine(db_url)

def load_data_to_db(df, table_name, engine):
    """Carga los datos transformados a la base de datos."""
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"Datos cargados en la tabla {table_name}.")
