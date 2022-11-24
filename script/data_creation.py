from script.file_creation import create_df, data_pos
from script.env import load_data_path
from script.inventoryOnhand import inventoyonhand_data_build
from datetime import datetime, timedelta


def inventory_on_hand_data(n, d):
    item_loc_data = inventoyonhand_data_build(n, d)
    return item_loc_data


def create_data(entities, n, m):
    column_pos = data_pos(entities)
    file_path = load_data_path()
    for i in range(0, m):
        d = datetime.today() - timedelta(days=i)
        time = d.strftime('%Y%m%d_%H%M%S%f')[:-3]
        file_name = entities[i]+'-' + time + '-' + str(i) + '.csv'
        df = create_df(entities)
        header = list(df.columns)
        data = inventory_on_hand_data(n, d)
        for j in range(0, len(column_pos)):
            df[header[column_pos[j]]] = data[j]
        df.to_csv(file_path + '/' + file_name, encoding='utf-8', index=False, sep='|')
