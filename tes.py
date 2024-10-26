import pandas as pd
file_path = 'static/dataset/game_dataset.xlsx' 
df = pd.read_excel(file_path)

print(df.dtypes)
