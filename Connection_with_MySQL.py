# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:46:46 2019

@author: rohti
"""

import pandas as pd
import mysql.connector
from mysql.connector import Error

#checking if the DB exists 
strDBName="MyDB"
strTableName="demo_data"

try:
    connection = mysql.connector.connect(host='localhost',
                                         database=strDBName,
                                         user='root',
                                         password='password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)

df = pd.read_sql('SELECT * FROM TableName')