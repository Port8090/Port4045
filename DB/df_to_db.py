import pandas as pd
import pymysql
from sqlalchemy import create_engine

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
# import MySQLdb

#engine = create_engine("mysql+mysqldb://admin:"+"admin123"+"@13.125.50.14:3306/foodpic", encoding='utf-8')
engine = create_engine("mysql://admin:admin123@13.125.50.14:3306/foodpic")
conn = engine.connect()

nutr_df = pd.read_csv("nutritionDB_forsql.csv")
print(nutr_df.head(3))

nutr_df.to_sql(name="nutrition", con=engine, if_exists='append')