import json
import requests
from urllib.error import HTTPError
import sys
import time



api_key = 'AIzaSyD6lXIN2SuT-2jMeXFvLA4-Hevc9viKgts'
url = ('https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze' +'?key=' + api_key)

## a funcition that takes a tweet (string) and output a dictionary of all the scores from perspective API
def get_perspective_score(tweet):
  retries = 1
  success = False
  score_dict = {}
  data_dict = {
    'comment': {'text': tweet},
    'languages': ['en'],
    'requestedAttributes': {'TOXICITY': {}, 'IDENTITY_ATTACK':{}, 'INSULT':{}, 'PROFANITY':{}, 'THREAT':{}, 'SEXUALLY_EXPLICIT':{},'FLIRTATION':{}}
  }

  while not success:
    try:
      response = requests.post(url=url, data=json.dumps(data_dict))
      response.raise_for_status()
      response_dict = json.loads(response.content)
      for key in response_dict['attributeScores']:
        value = response_dict['attributeScores'][key]['summaryScore']['value']
        key = key.lower()
        score_dict[key] = value
      success = True
    
    except Exception as err:
      print(f'Other error occurred: {err}')
      wait = retries * 30;
      print('Error! Waiting %s secs and re-trying...' % wait)
      sys.stdout.flush()
      time.sleep(wait)
      retries += 1

  # print(score_dict)
  return score_dict



# get_perspective_score('Hello what si worng with you')