import pandas as pd
import numpy as np

imdb_df = pd.read_csv('IMDB_Dataset.csv', index_col = None)
imdb_df = imdb_df.head(10000)