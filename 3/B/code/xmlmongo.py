import pandas as pd
import xml.etree.ElementTree as et 
import pymongo
from pymongo import MongoClient
import json

xtree = et.parse("/home/fsociety/Documents/Precog/stackoverflow.com/Posts.xml")
xroot = xtree.getroot()
chil = xroot.getchildren()
# df_cols= ['Id','TagName','Count','ExcerptPostId','WikiPostId']
i=0
while i < len(chil):

    df_cols = chil[i].attrib
    print(df_cols)

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Posts"]
    mycol = mydb["data"]
    i+=1
    x = mycol.insert_one(df_cols)

