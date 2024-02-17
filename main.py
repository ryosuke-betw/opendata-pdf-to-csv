import pandas as pd
import tabula

# lattice=Trueでテーブルの軸線でセルを判定
dfs = tabula.read_pdf("000876235.pdf", lattice=True, pages='all', pandas_options={'header': None})
i = 0
for df in dfs:
    i += 1
    df = df.replace( '\n', '', regex=True).replace( '\r', '', regex=True).replace( '\r\n', '', regex=True).replace( '\n\r', '', regex=True)
    print(df)
    df.to_csv(str(i)+".csv", index=None)