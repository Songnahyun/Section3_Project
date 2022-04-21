import csv
import os
from pymongo import MongoClient

HOST = 'cluster0.tw6ak.mongodb.net'
USER = 'songnahyun'
PASSWORD = 'songnahyun1234'
DATABASE_NAME = 'myProject'
COLLECTION_NAME = 'cosmetics'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

import pandas as pd
import json 

df = pd.read_csv('DATA.csv')
df_json = df.to_json(orient = "records")
data = json.loads(df_json)

collection.insert_many(data)


