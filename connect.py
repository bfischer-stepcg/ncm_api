#! /usr/bin/python3
import json
import requests

headers = {
  'X-CP-API-ID': '',
  'X-CP-API-KEY': '',
  'X-ECM-API-ID': '',
  'X-ECM-API-KEY': '',
  'Content-Type': 'application/json' 
}

BASE_URL = 'https://www.cradlepointecm.com/api/v2/{0}'

def get(url,data_fields):
  """
  Takes the url and data fields requested, then creates an array of dicts
  containing the data fields. Utilizes the API next url to get additional
  responses.  Finally returns the array of responses
  """
  data_array = []
  while url:
    req = requests.get(
      url,
      headers=headers
      )
    resp = req.json()
    return(resp)
    for i in range(len(resp['data'])):
      data_values = {}
      for x in data_fields:
        data_values[x] = resp['data'][i][x]
      data_array.append(data_values)
    url = resp['meta']['next']
  return data_array

def put(url,payload):
  """
  """
  while url:
    req = requests.put(
      url,
      headers=headers,
      data=payload
      )
    resp = req.json()
    if req.status_code != 200:
      return req.raise_for_status()
    else:
      return resp