import pandas as pd

# 读 CSV
df = pd.read_csv("pirvision_office_dataset1.csv")

# 写成 Parquet
df.to_parquet("pirvision_office_dataset1.parquet", engine="pyarrow", index=False)

# 读取 Parquet
df2 = pd.read_parquet("pirvision_office_dataset1.parquet", engine="pyarrow")
print(df2.head())
