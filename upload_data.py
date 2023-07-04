from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resoure indentifier
uri = "mongodb+srv://ankitskusahu7846:Ankitkusahu@cluster0.vcb28wv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collenction name
DATABASE_NAME = "pwskillstwo"
COLLECTION_NAME = "waferdata"

# read data as a dataframe
df = pd.read_csv(r"E:\Wafer_Fault_Predection\notebooks\wafer_23012020_041211.csv")
df = df.drop("Unnamed: 0", axis=1)

# convert data into json
json_record = list(json.loads(df.T.to_json()).values())

# now dump the data intp the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
