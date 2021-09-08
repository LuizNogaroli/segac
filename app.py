import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
  
conn=psycopg2.connect(
    database="dfe9m5a8ccaesp",
    user="ywjatqzfybsppl",
    password="c41a3ff31a8806e65e2e11c0c168783fde194aa3d62174ae0483c832d18ddedf",
    host="ec2-52-3-130-181.compute-1.amazonaws.com",
    port="5432"
)

# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

# Creating a cursor object using the cursor() 
# method
cursor = conn.cursor()  
# drop table accounts
sql = '''DROP TABLE IF EXISTS asdas'''  
# Executing the query
cursor.execute(sql)
print("Table dropped !")  
# Commit your changes in the database
conn.commit()  
# Closing the connection
conn.close()

df = pd.read_excel('vagas.xls')
# print(df)


from sqlalchemy import create_engine

engine = create_engine('postgresql://ywjatqzfybsppl:c41a3ff31a8806e65e2e11c0c168783fde194aa3d62174ae0483c832d18ddedf@ec2-52-3-130-181.compute-1.amazonaws.com:5432/dfe9m5a8ccaesp')

df.to_sql('vagas', engine, if_exists='append')

print(df[['ÁREA', 'MODALIDADE']].groupby('ÁREA'))