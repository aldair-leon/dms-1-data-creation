from script.env import load_resources_path
import pandas as pd
from script.logger import log
import random

logger = log('ENV SETUP')


def itemloc_combinations():
    path = load_resources_path()
    logger.info('item_loc')
    df = pd.read_csv(path + '/' + 'inventoryonhand.csv', sep='|')  # TRANSACTIONAL
    item_loc = df.drop_duplicates(['PRODUCTID', 'LOCATION'])
    return item_loc


def itemloc_data_load_data():
    path = load_resources_path()
    logger.info('item_loc')
    df = pd.read_csv(path + '/' + 'inventoryonhand.csv', sep='|')
    df = df.sample(frac=1)
    new_df = df.reset_index(drop=True)
    return new_df


def inventoyonhand_data_build(n, d):
    available = d.strftime('%Y-%m-%d')
    timestamp_ = d.strftime('%Y-%m-%dT23:00:00+02:00')
    unitype = ['EA', 'KG']
    df = itemloc_data_load_data()
    df = df.iloc[:int(n)]
    pruductid = df['PRODUCTID'].tolist()
    location = df['LOCATION'].tolist()
    availabledate = [available for i in range(int(n))]
    unitofmeasure = [random.choice(unitype) for i in range(int(n))]
    quantity = [1 for i in range(int(n))]
    timestamp = [timestamp_ for i in range(int(n))]
    return pruductid, location, availabledate, unitofmeasure, quantity, timestamp
