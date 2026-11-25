import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()


engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5433/{os.getenv('POSTGRES_DB')}"
)

data_file = pd.read_csv("employee_attrition_dataset_10000.csv")

data_file.columns = [col.lower().replace(" ", "_") for col in data_file.columns]

data_file.to_sql(
    name="employees",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000,
    method="multi"
)