import requests
import pprint
import pandas as pd

api_key = '18c511a7ccde4f895ac8e633d45e936c'

movie_id = 500
api_version = 3

api_base_url = 'https://api.themoviedb.org/{}'.format(api_version)
endpoint_path = '/search/movie/'
search_query = "The Matrix"
endpoint = "{}{}?api_key={}&query={}".format(api_base_url,endpoint_path,api_key,search_query)
r = requests.get(endpoint)
#print(r.status_code)
#pprint.pprint(r.json())
if r.status_code in range(200,299):
   data = r.json()
   results = data['results']
   if len(results) > 0:
      #print(results[0].keys())
      movie_ids = set()
      for result in results:
         _id = result['id']
         #print(result['title'],_id)
         movie_ids.add(_id)
      #print(list(movie_ids))

output = 'movies_csv'
movie_data = []

for movie_id in movie_ids:
    api_version = 3
    api_base_url = 'https://api.themoviedb.org/{}'.format(api_version)
    endpoint_path = '/movie/{}'.format(movie_id)
    endpoint = "{}{}?api_key={}".format(api_base_url,endpoint_path,api_key)
    r = requests.get(endpoint)
    if r.status_code in range(200,299):
       data = r.json()
       movie_data.append(data)
    #pprint.pprint(r.json())
df = pd.DataFrame(movie_data)
#print(df.head())
df.to_csv(output,index=False)
