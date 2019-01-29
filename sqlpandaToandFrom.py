'''
Author: Nishant Singh
Date: 12.01.2019
get data from sql server to pandas
get data from pandas data frame to sql server database
'''

## From SQL to DataFrame Pandas

import pandas as pd
import pyodbc

sql_connect = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=SQLSERVER2017;DATABASE=SchoolABC;Trusted_Connection=yes') 
query = "SELECT [StudentID],[NameFirst],[NameLast],[Post],[City] FROM [Fee].[vClerkName]"
df = pd.read_sql(query, sql_connect)

df.head(3)

## From DataFrame Pandas to SQL

'''
Have table prepared ON Microsoft SQL Server
USE SchoolABC;
GO
DROP TABLE IF EXISTS vClerkName_test
CREATE TABLE vClerkName_test
(
 [StudentID] INT
,[NameFirst] VARCHAR(50)
,[NameLast] VARCHAR(100)
)
'''
connectionSt = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=SQLSERVER2017;DATABASE=SchoolABC;Trusted_Connection=yes')
cursor = connectionSt.cursor()

for index,row in df.iterrows():
    cursor.execute("INSERT INTO dbo.vClerkName_test([StudentID],[NameFirst],[NameLast]) values (?, ?,?)", row['StudentID'], row['NameFirst'] , row['NameLast']) 
    connectionSt.commit()

cursor.close()
connectionSt.close()