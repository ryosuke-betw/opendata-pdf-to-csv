import pandas as pd
import tabula
import os
from constants import PREFECTURES


def delete_headers(df, line_number):
    if df.iloc[0, 0] == "基本情報":
        return df.drop(df.index[:line_number])
    return df


if not os.path.exists("./output_files"):
    os.mkdir("./output_files")

for i in range(1, 47):
    print("PREFECTURE_NUMBER", i)
    opendata_file = os.listdir(f"./data_files/shinryoujo_{i}")
    dfs = tabula.read_pdf(f"./data_files/shinryoujo_{i}/{opendata_file[0]}", lattice=True, pages='all', pandas_options={'header': None})
    # 1ページ目のみ「基本情報」行の削除のため1行指定
    first_df = delete_headers(dfs[0], 1)
    # 2ページ目以降は「基本情報」およびヘッダーを削除するため2行指定
    dfs = [delete_headers(x, 2) for x in dfs[1:]]
    dfs.insert(0, first_df)
    merged_df = pd.concat(dfs).replace('\n', '', regex=True).replace('\r', '', regex=True).replace('\r\n', '', regex=True).replace('\n\r', '', regex=True)
    result_df = merged_df.dropna(subset=[0])
    result_df.to_csv(f"./output_files/{PREFECTURES[i-1]}.csv", header=False, index=False)
