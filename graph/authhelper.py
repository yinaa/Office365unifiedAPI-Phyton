from urllib.parse import quote, urlencode
import requests

# Client ID and secret
client_id = 'e5ac0615-e826-4ded-9632-7da43e0c216e'
client_secret = 'JuS7LSrM00z/BxIiziq0zOX+tEurCmEiJgK3OFfExUg='

# Constant strings for OAuth2 flow
# The OAuth authority
authority = 'https://login.microsoftonline.com'

# The authorize URL that initiates the OAuth2 client credential flow for admin consent
authorize_url = '{0}{1}'.format(authority, '/common/oauth2/authorize?{0}')

# The token issuing endpoint
token_url = '{0}{1}'.format(authority, '/common/oauth2/token')

def get_signin_url(redirect_uri):
  # Build the query parameters for the signin url
  params = { 'client_id': client_id,
             'redirect_uri': redirect_uri,
             'response_type': 'code',
             'prompt': 'login',
           }

  signin_url = authorize_url.format(urlencode(params))

  return signin_url

def get_token_from_code(auth_code, redirect_uri):
  # Build the post form for the token request
  post_data = { 'grant_type': 'authorization_code',
                'code': auth_code,
                'redirect_uri': redirect_uri,
                'resource': 'https://graph.microsoft.com',
                'client_id': client_id,
                'client_secret': client_secret
              }
  r = requests.post(token_url, data = post_data)
  try:
    access_token = r.json()['access_token']
    return access_token
  except:
    return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text)
