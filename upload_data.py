#read the dataset first and then upload it to mongo db
# go to mongobb ->sign in-> then go to ->https://cloud.mongodb.com/v2/66dc1a45609cce46cfc88c59#/setup/personalization


from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url , after creating a cluster u will get it
uri = "mongodb+srv://mahak:12345@cluster0.0x9celj.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to server
client = MongoClient(uri)

# create database name and collection name, u have to give it just here 
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv('C:\Users\Mahak Dashore\OneDrive\Desktop\VscodeProjects\SensorFault\notebooks\wafer_23012020_041211.csv')

df.drop('Unnamed: 0', axis=1, inplace=True)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


