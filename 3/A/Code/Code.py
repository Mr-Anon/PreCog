import tabula 
from tabula import convert_into
import pandas as pd

file_path = "/home/fsociety/Documents/Precog/Rec_Task/Rec_Task/EICHERMOT.pdf"
df = tabula.read_pdf(file_path,pages='all')
convert_into(file_path, "table4.csv", output_format="csv",pages='all')

from pymongo import MongoClient
data = pd.read_csv('table4.csv')
client =  MongoClient()
db = client['Tables']
collection = db['Table4']
data.reset_index(inplace=True)
data_dict = data.to_dict("records")
collection.insert_many(data_dict)