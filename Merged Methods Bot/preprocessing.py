import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#https://www.kaggle.com/tmdb/tmdb-movie-metadata
credits = pd.read_csv("tmdb_5000_credits.csv")

movies_df = pd.read_csv("tmdb_5000_movies.csv")


credits_column_renamed = credits.rename(index=str, columns={"movie_id": "id"})
movies_df_merge = movies_df.merge(credits_column_renamed, on='id')

movies_cleaned_df = movies_df_merge.drop(columns=['homepage', 'title_x', 'title_y', 'status','production_countries'])

v=movies_cleaned_df['vote_count']
R=movies_cleaned_df['vote_average']
C=movies_cleaned_df['vote_average'].mean()
m=movies_cleaned_df['vote_count'].quantile(0.80)

movies_cleaned_df['weighted_average']=((R*v)+ (C*m))/(v+m)

weight_average=movies_cleaned_df.sort_values('weighted_average',ascending=False)

popularity=movies_cleaned_df.sort_values('popularity',ascending=False)

scaling=MinMaxScaler()

movie_scaled_df=scaling.fit_transform(movies_cleaned_df[['weighted_average','popularity']])
movie_normalized_df=pd.DataFrame(movie_scaled_df,columns=['weighted_average','popularity'])

movies_cleaned_df[['normalized_weight_average','normalized_popularity']]= movie_normalized_df

movies_cleaned_df['score'] = movies_cleaned_df['normalized_weight_average'] * 0.5 + movies_cleaned_df['normalized_popularity'] * 0.5

movies_scored_df = movies_cleaned_df.sort_values(['score'], ascending=False)

scored_df = movies_cleaned_df.sort_values('score', ascending=False)
scored_df.to_csv("preprocessed.csv")