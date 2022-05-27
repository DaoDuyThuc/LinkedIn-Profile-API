import requests
import json

PROXYCURL_API_KEY = 'paste your API key here' 

filename = 'profile.json'

def get_profile(profile_id):
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    params = {
        'url': f'https://www.linkedin.com/in/{profile_id}',
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    return response.json()

result = get_profile('paste a profile ID here')

# save to a new json file
with open(filename, 'a') as f_obj: # append
    json.dump(result, f_obj, indent = 2)
