import requests

api_key = 'YOUR_API_KEY'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'twitter_profile_url': 'https://x.com/johnrmarty/',
    'facebook_profile_url': 'https://facebook.com/johnrmarty/',
    'linkedin_profile_url': 'https://linkedin.com/in/johnrmarty/',
    'extra': 'include',
    'github_profile_id': 'include',
    'facebook_profile_id': 'include',
    'twitter_profile_id': 'include',
    'personal_contact_number': 'include',
    'personal_email': 'include',
    'inferred_salary': 'include',
    'skills': 'include',
    'use_cache': 'if-present',
    'fallback_to_cache': 'on-error',
}
response = requests.get(
    "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json")

print(response.json()['full_name'])
