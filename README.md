# NPS_pipeline
 Webscraping with python and beautiful soup to gather json data from nps.gov using the nps.gov api
 
 nps_data_grab.py sends requests to nps.gov to gather all data excluding webcams listed in the API documentation as of 11/29/2021
 
https://www.nps.gov/subjects/developer/api-documentation.htm

Then data is then formatted as json type with indent = 4 for readablility and stored in the raw_json folder
