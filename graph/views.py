from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from graph.authhelper import get_signin_url, get_token_from_code
from graph.graphservice import get_me, get_messages, get_files
import pprint

# Create your views here.

def home(request):
  redirect_uri = request.build_absolute_uri(reverse('graph:gettoken'))
  sign_in_url = get_signin_url(redirect_uri)
  return HttpResponse('<a href="' + sign_in_url +'">Click here to sign in and view your data</a>')

def gettoken(request):
  auth_code = request.GET['code']
  redirect_uri = request.build_absolute_uri(reverse('graph:gettoken'))
  access_token = get_token_from_code(auth_code, redirect_uri)
  # Save the token in the session
  request.session['access_token'] = access_token
  return HttpResponseRedirect(reverse('graph:me'))

def me(request):
  access_token = request.session['access_token']
  # If there is no token in the session, redirect to home
  if not access_token:
    return HttpResponseRedirect(reverse('graph:home'))
  else:
    me = get_me(access_token)
    return HttpResponse('User: {0}'.format(me))

def mail(request):
  access_token = request.session['access_token']
  # If there is no token in the session, redirect to home
  if not access_token:
    return HttpResponseRedirect(reverse('graph:home'))
  else:
    messages = get_messages(access_token)
    return HttpResponse('Messages: {0}'.format(messages))

def files(request):
  access_token = request.session['access_token']
  # If there is no token in the session, redirect to home
  if not access_token:
    return HttpResponseRedirect(reverse('graph:home'))
  else:
    files = get_files(access_token)
    return HttpResponse('Messages: {0}'.format(files))
