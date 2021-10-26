
#import xml file from skybitz website
#
# source is below

# from https://stackoverflow.com/questions/51976146/python-insert-into-ms-access-table
import xml.etree.ElementTree as ET

from urllib.request import urlopen
#you need to import those libraries using pip install command

import sys, os, pyodbc 

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ= C:/Users/Abdou/samsara.accdb;'
    )
connection = pyodbc.connect(conn_str)


  

url = "the URl to xml file in the website"

with urlopen(url) as f:
    #parse the xml as tree
    tree = ET.parse(f)
    root = tree.getroot()
    i=0
    cursor = connection.cursor()

    #test sql
    sql="Insert into trailer (assetid, battery, latitude, longitude) values ('53096','OK','41.66991','-88.02142')"
    print (sql)
    cursor.execute(sql)

    #get data from every child by tag
    for country in root.findall('gls'):
        assetid = country.find('assetid').text
        battery = country.find('battery').text
        try:
            latitude = country.find('latitude').text
        except Exception as e:
            latitude=0
        try:
            longitude = country.find('longitude').text
        except Exception as e:
            longitude=0
        
        print(assetid, ", ",battery,", ",latitude,", ",longitude)
        # increment number of child read
        i=i+1
        sql="Insert into trailer (assetid, battery, latitude, longitude) values ('"+str(assetid)+"','"+str(battery)+"','"+str(latitude)+"','"+str(longitude)+"')"
        print (sql)
        cursor.execute(sql)
# i = total number of row inserted        
print (i)
#validate the insertion on the database
connection.commit() 


