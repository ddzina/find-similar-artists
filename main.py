import pandas as pd
from funcs import get_similar_artists, get_rating_dict

if __name__ == '__main__':
    df = pd.read_csv('lastfm_user_scrobbles.csv')
    names_df = pd.read_csv('lastfm_artist_list.csv')

    user_rating = get_rating_dict()

    flag = True
    while flag:
        input_artist = input().strip()
        try:
            artist_id = (names_df[names_df['artist_name']==input_artist].index + 1).tolist()
            fans = df[df['artist_id']== artist_id[0]]
            flag = False
        except IndexError:
            print('I know nothing about this artist, please check the name')
            flag = True
    
    fans.sort_values('scrobbles', ascending=False)
    top_fan = fans.iloc[0]
    top_artists_id = get_similar_artists(str(top_fan.user_id), user_rating)
    artists = []
    for index in top_artists_id:
        temp_df = names_df[names_df['artist_id'] == int(index)]
        artists.append(temp_df['artist_name'].iloc[0])
    print(', '.join(artists))
