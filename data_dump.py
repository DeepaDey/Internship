import pymongo
import pandas as pd
import json
from src.config import mongo_client
#from dotenv import load_dotenv
#print(f"Loading environment variable from .env file")
#load_dotenv()
#Provide the mongodb localhost url to connect python to mongodb.
#mongo_client = pymongo.MongoClient("mongodb+srv://Ineuron:Ineuron1@cluster0.bbbhw0k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DATA_FILE_PATH="D:/internship/mlproject/notebook/UCI_Credit_Card.csv"
DATABASE_NAME="creditcard"
COLLECTION_NAME="frauddetection"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")
    
    
#Convert dataframe to json so that we can dump these record in mongo db
df.reset_index(drop=True,inplace=True)

json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])

#insert converted json record to mongodb
mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    