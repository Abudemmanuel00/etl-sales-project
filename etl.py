import pandas as pd
from sqlalchemy import create_engine

# 1) Leer CSV
df = pd.read_csv("sales_data.csv")

# 2) Convertir fecha a formato correcto (YYYY-MM-DD)
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"], errors="coerce").dt.date

# 3) Conexión MySQL (tu password es 1234)
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/etl_project")

# 4) Subir datos a la tabla ya creada
df.to_sql(name="sales_data", con=engine, if_exists="append", index=False)

print("Datos cargados correctamente!")
