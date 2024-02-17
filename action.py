import pandas as pd
import glob
import os


def integrate(input_file_path, output_file_name):
    number = sum(os.path.isfile(os.path.join(input_file_path, name)) for name in os.listdir(input_file_path))
    data_list = []

    for i in range(0, number):
        data_list.append(pd.read_csv(f"{input_file_path}/{i+1}.csv"))

    df = pd.concat(data_list, axis=0, sort=True)

    df.to_csv(f"{output_file_name}", index=False)
