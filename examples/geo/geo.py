import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Retrieve email statistics by country and state/province. #
# GET /geo/stats #

params = {'end_date': '2016-04-01', 'country': 'US', 'aggregated_by': 'day', 'limit': 1, 'offset': 1, 'start_date': '2016-01-01'}
response = sg.client.geo.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

