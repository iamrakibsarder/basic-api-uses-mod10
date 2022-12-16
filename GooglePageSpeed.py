import requests
api_key = ' AIzaSyB88GGDjBK9hj2uIezrI4aGOl_PWNilA1w '
url = 'https://developers.google.com'
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}'
res = requests.get(api_url)
data = res.json()
cls_score = data.get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('percentile')
print(cls_score)