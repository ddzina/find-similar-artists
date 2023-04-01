import pandas as pd
import csv
import math

def cosine_distance(vecA, vecB):
    def dot_product(vecA, vecB):
        d = 0.0
        for dim in vecA:
            if dim in vecB:
                d += vecA[dim]*vecB[dim]
        return d
    return dot_product(vecA,vecB) / math.sqrt(dot_product(vecA,vecA)) / math.sqrt(dot_product(vecB,vecB))


def get_rating_dict(filename = "lastfm_user_scrobbles.csv"):
    with open(filename, 'r') as f:
        r = csv.reader(f)
        output = dict()
        for i, line in enumerate(r):
            if i == 0:
                continue
            user    = line[0]
            artist = line[1]
            rate    = int(line[2])
            if not user in output:
                output[user] = dict()
            output[user][artist] = rate
    return output


def get_similar_artists(user_id, user_ratings):
    # Find like-minded users
    user_matches = [(u, cosine_distance(user_ratings[user_id], user_ratings[u])) for u in user_ratings if u != user_id]
    best_user_matches = sorted(user_matches, key=lambda x: x[1], reverse=True)[:1000]

    # normalization coef
    total_similarity = sum([x[1] for x in best_user_matches])
    
    # filtering closer users
    best_user_matches = dict([x for x in best_user_matches if x[1] > 0.25])

    # find top artists
    artist_similarity = dict()
    for related_user in best_user_matches:
        for artist in user_ratings[related_user]:
            if not artist in user_ratings[user_id]:
                if not artist in artist_similarity:
                    artist_similarity[artist] = 0.0
                artist_similarity[artist] += user_ratings[related_user][artist] * best_user_matches[related_user]
    
    # normalization
    for artist in artist_similarity:
        artist_similarity[artist] /= total_similarity
    
    # sort to get most relevant
    top_artists = sorted(artist_similarity.items(), key=lambda x: x[1], reverse=True)[:5]
    return [x[0] for x in top_artists]