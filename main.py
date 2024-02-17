import pandas as pd
import tabula
import os
from prefecture import prefectures


if not os.path.exists("./output_files"):
    os.mkdir("./output_files")

for i in range(1, 47):
    opendata_file = os.listdir(f"./data_files/shinryoujo_{i}")
    dfs = tabula.read_pdf(f"./data_files/shinryoujo_{i}/{opendata_file[0]}", lattice=True, pages='all', pandas_options={'header': None})
    merged_df = pd.concat(dfs).replace('\n', '', regex=True).replace('\r', '', regex=True).replace('\r\n', '', regex=True).replace('\n\r', '', regex=True)
    merged_df.to_csv(f"./output_files/{prefectures[i-1]}.csv", index=None)

