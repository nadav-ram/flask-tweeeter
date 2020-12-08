import pandas
import moderation
import random
from datetime import datetime 

df = pandas.read_csv('data/sampled-tweets-balanced.csv')

new_df = pandas.DataFrame(columns=['id', 'date_posted', 'content', 'user_id', \
'retweet', 'comment', 'toxicity', 'threat', 'sexually_explicit','profanity', \
'insult', 'identity_attack', 'flirtation'])

for index, row in df.iterrows():
    print(index)
    score_dict = moderation.get_perspective_score(row['tweet'])
    new_df = new_df.append({
        'id': row['id'],
        'date_posted':datetime.utcnow,
        'content': row['tweet'],
        'user_id': random.randint(0, 9), 
        'retweet': None,
        'comment': None,
        'toxicity': score_dict['toxicity'],
        'threat': score_dict['threat'],
        'sexually_explicit': score_dict['sexually_explicit'],
        'profanity': score_dict['profanity'],
        'insult': score_dict['insult'],
        'identity_attack': score_dict['identity_attack'],
        'flirtation': score_dict['flirtation']
    }, ignore_index=True)

new_df.to_csv('new.csv')
