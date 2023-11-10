import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])  


import_or_install('mysql-connector-python') 
import_or_install('pandas') 
import_or_install('matplotlib') 
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt



## crear data frame

df = pd.read_csv('big_bang_theory_dataset.csv')
# get first row using row position
df.rename(columns={'Unnamed: 0': "ID"}, inplace=True)
df.fillna('', inplace=True)
columns = list(df.columns)

##columns[0] = 'ID'

columns = ','.join(columns)

print(columns) 
#print(df) 

## sql

'''
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database='big_bang'
)


mycursor = conn.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS big_bang")

mycursor.execute("CREATE TABLE IF NOT EXISTS bbt_dataset (ID int NOT NULL,Location varchar (500), Scene varchar (500), Text varchar (500), Speaker varchar(100), Season int, PRIMARY KEY (ID))")


sql =''
for index, row in df.iterrows():
    str_values = df.loc[index, :].values.flatten().tolist()

    count = 0
    values = ''
    for i  in str_values: ##crear el string SQL
        if count == 0:
            values = values +str(i)+","
        elif count == len(str_values)-1:
            values = values +str(i)
        else:
            if i == 'nan':
            values = values+"'"+str(i)+"',"
        count += 1
    sql = "INSERT IGNORE INTO big_bang.bbt_dataset ("+columns+") VALUES ("+values+");"
    #ejecutar el query
    mycursor.execute(sql)
    #aplicar los cambios en la db
    conn.commit()
#cierre de conexion 
conn.close()
print ('termine')
    '''

# create a dataframe 
sheldon_df = df[df['Speaker'] == 'Sheldon']
sheldon_df = pd.DataFrame(sheldon_df, columns = ['Text','Location']) 
sh_penny_df = sheldon_df[sheldon_df['Text'] == 'Penny.']
contiene_sh_penny_df = sheldon_df[df['Text'].str.contains("Penny")==True]

ax = sh_penny_df.hist(column='Text', by='Location', bins=25, grid=False, figsize=(8,10), layout=(5,1), sharex=True, color='#86bf91', zorder=2, rwidth=0.9)
