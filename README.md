# django
## Azure AD Authentication - https://www.youtube.com/watch?v=cy7Xk35iiGc
## Docs - https://django-auth-adfs.readthedocs.io/en/latest/install.html
## AD - https://www.youtube.com/watch?v=t02stKhdxi4&t=1895s

## What all changes needed for Azure ADlogin
## Create App registration
```
pip install django_auth_adfs

## Update in the Settings.py
INSTALLED_APPS = (
    ...
    # Needed for the ADFS redirect URI to function
    'django_auth_adfs',



## Update to the bottom of the settings.py
AUTHENTICATION_BACKENDS = (
    ...
    'django_auth_adfs.backend.AdfsAuthCodeBackend',
    ...
LOGIN_URL = "django_auth_adfs:login"
LOGIN_REDIRECT_URL = "/"


```
## Settings.py
```
# Client secret is not public information. Should store it as an environment variable.

client_id = 'Your client id here'
client_secret = 'Your client secret here'
tenant_id = 'Your tenant id here'


AUTH_ADFS = {
    'AUDIENCE': client_id,
    'CLIENT_ID': client_id,
    'CLIENT_SECRET': client_secret,
    'CLAIM_MAPPING': {'first_name': 'given_name',
                      'last_name': 'family_name',
                      'email': 'upn'},
    'GROUPS_CLAIM': 'roles',
    'MIRROR_GROUPS': True,
    'USERNAME_CLAIM': 'upn',
    'TENANT_ID': tenant_id,
    'RELYING_PARTY_ID': client_id,
}

```
##  Settings.py
```
AUTHENTICATION_BACKENDS = [
    ...
    'django_auth_adfs.backend.AdfsAccessTokenBackend',
    ...
]
```
## urls.py
```
from django.conf.urls import include
urlpatterns = [
    ...
    path('oauth2/', include('django_auth_adfs.urls')),
    ...
]
```
## 










```
