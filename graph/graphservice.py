import requests
import uuid

graph_api_endpoint = 'https://graph.microsoft.com/beta/{0}'

# Generic API Sending
def make_api_call(method, url, token, payload = None, parameters = None):
    # Send these headers with all API calls
    headers = { 'User-Agent' : 'jurassichack/1.0',
                'Authorization' : 'Bearer {0}'.format(token),
                'Accept' : 'application/json' }

    # Use these headers to instrument calls. Makes it easier
    # to correlate requests and responses in case of problems
    # and is a recommended best practice.
    request_id = str(uuid.uuid4())
    instrumentation = { 'client-request-id' : request_id,
                        'return-client-request-id' : 'true' }

    headers.update(instrumentation)

    response = None

    if (method.upper() == 'GET'):
        response = requests.get(url, headers = headers, params = parameters)
    elif (method.upper() == 'DELETE'):
        response = requests.delete(url, headers = headers, params = parameters)
    elif (method.upper() == 'PATCH'):
        headers.update({ 'Content-Type' : 'application/json' })
        response = requests.patch(url, headers = headers, data = payload, params = parameters)
    elif (method.upper() == 'POST'):
        headers.update({ 'Content-Type' : 'application/json' })
        response = requests.post(url, headers = headers, data = payload, params = parameters)

    return response

# Get /me
def get_me(access_token):
  get_me_url = graph_api_endpoint.format('/me')

  r = make_api_call('GET', get_me_url, access_token)

  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

#Get /mail
def get_messages(access_token):
  get_messages_url = graph_api_endpoint.format('/me/messages')

  # Use OData query parameters to control the results
  #  - Only first 10 results returned
  #  - Only return the DateTimeReceived, Subject, and From fields
  #  - Sort the results by the DateTimeReceived field in descending order
  query_parameters = {'$top': '10',
                      '$select': 'DateTimeReceived,Subject,From',
                      '$orderby': 'DateTimeReceived DESC'}

  r = make_api_call('GET', get_messages_url, access_token, parameters = query_parameters)

  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

#Get /files
def get_files(access_token):
  get_messages_url = graph_api_endpoint.format('/me/files')

  r = make_api_call('GET', get_messages_url, access_token)

  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)
