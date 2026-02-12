import numpy as np
import pandas as pd
from sqlalchemy import create_engine

path = 'C:/Personal/PythonProjCustomerBehaviourAnalysis/customer_shopping_behavior.csv'
data = pd.read_csv(path)

data.head()

data['Review Rating'] = data.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

data.columns = data.columns.str.lower()
data.columns = data.columns.str.replace(' ','_')
data = data.rename (columns = {'purchase_amount_(usd)':'purchase_amount'})

#create a column age group

labels = ['Young_Adult', 'Adult', 'Middle_Aged', 'Senior']
data['age_group']=pd.qcut(data['age'],q=4,labels=labels)

#create column purchase_frequency_days
frequency_mapping = {'Fortnightly' : 14, 'Weekly':7, 'Monthly':30, 'Quarterly':90, 'Bi-Weekly': 14, 'Annually': 365, 'Every 3 Months': 90 }
data['purchase_frequency_days'] = data['frequency_of_purchases'].map(frequency_mapping)

data = data.drop('promo_code_used', axis=1)



#MySQL Connection

username = "root"
password = "Root"
host = "127.0.0.1"
port = "3306"
database = "customer_behavior_analysis"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

#Write DataFrame to MySQL

table_name = "customer_data" #choose any table name
data.to_sql(table_name, engine, if_exists='replace', index=False)
