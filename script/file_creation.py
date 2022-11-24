import pandas as pd
from script.env import load_entities_json


def create_df(entities):
    json_file = load_entities_json()
    for i in range(0, len(entities)):
        header = json_file[entities[i]]['columns']
        df = pd.DataFrame(columns=header)
    return df


def data_pos(entities):
    json_file = load_entities_json()
    for i in range(0, len(entities)):
        column_pos = json_file[entities[i]]['columns_position']
    return column_pos
