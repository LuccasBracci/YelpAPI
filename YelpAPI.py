from yelpapi import YelpAPI
import pandas as pd
import json

# Load API key from JSON file
with open('.secret/yelp_api.json') as f:
    api_key = json.load(f)['api-key']

# Initialize YelpAPI client
yelp_api = YelpAPI(api_key)

# Define search parameters
location = 'New York, NY'
term = 'Italian'
categories = 'restaurants'
limit = 50

# Define empty list to store results
results = []

# Iterate over search results using offset parameter
for offset in range(0, 1000, limit):
    response = yelp_api.search_query(term=term, location=location, categories=categories,
                                     limit=limit, offset=offset)
    results += response['businesses']

# Compile results into a Pandas dataframe
df = pd.DataFrame.from_records(results)