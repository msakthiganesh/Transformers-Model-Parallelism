label = []

for index, row in imdb_df.iterrows():
    if(row['sentiment'] == 'positive'): label.append(1)
    else: label.append(0)

imdb_df['label'] = label
imdb_df = imdb_df.drop(['sentiment'], axis = 1)