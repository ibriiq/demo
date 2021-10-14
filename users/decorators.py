from functools import wraps
from django.http import HttpResponseRedirect



def Only_once_login_is_passed(function):
    def _function(request,*args, **kwargs):
        if request.session.get('user') is None:
            return HttpResponseRedirect('/login')
        return function(request, *args, **kwargs)
    return _function

def Already_authenticated_users_arenot_allowed(function):
    def _function(request,*args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return function(request, *args, **kwargs)
    return _function

def login_required(function):
    def _function(request,*args, **kwargs):
        if 'loggin_user' not in request.session:
            return HttpResponseRedirect('/login?next='+request.path)
        return function(request, *args, **kwargs)
    return _function
