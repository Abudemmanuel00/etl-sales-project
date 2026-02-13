# 📊 ETL Sales Data Pipeline Project

Este proyecto demuestra la implementación de un pipeline ETL (Extract, Transform, Load) utilizando Python, Pandas y MySQL para procesar datos de ventas almacenados en archivos CSV y cargarlos en una base de datos relacional.

---

## 🚀 Tecnologías utilizadas

- Python
- Pandas
- MySQL
- SQLAlchemy
- Git & GitHub

---

## 📂 Estructura del proyecto

```
etl-sales-project/
│
├── etl.py
├── datos_de_ventas.csv
└── README.md
```

---

## ⚙️ Proceso ETL

### 1️⃣ Extracción (Extract)
Se leen los datos desde un archivo CSV utilizando la librería Pandas.

```python
df = pd.read_csv("datos_de_ventas.csv")
```

---

### 2️⃣ Transformación (Transform)
Se transforman los datos para asegurar que las fechas estén en el formato correcto.

```python
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'], errors='coerce').dt.date
```

---

### 3️⃣ Carga (Load)
Los datos transformados se cargan en una base de datos MySQL utilizando SQLAlchemy.

```python
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/etl_project")

df.to_sql(
    name="sales_data",
    con=engine,
    if_exists="append",
    index=False
)
```

---

## 🗄️ Base de Datos

Base de datos utilizada: **etl_project**

Tabla creada: **sales_data**

---

## 📈 Resultado

Los datos del archivo CSV fueron cargados correctamente en MySQL y pueden ser consultados mediante:

```sql
SELECT * FROM sales_data;
```

---

## 🧠 Autor

**Emmanuel Abud**  
Estudiante de Ingeniería en Computación  
Proyecto de Portafolio - Data Engineering
