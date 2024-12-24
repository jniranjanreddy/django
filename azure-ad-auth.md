## How to configure Azure AD Authentication

## Create App registration with web.
![image](https://github.com/user-attachments/assets/64dda176-199e-4ea3-9e8e-01e93074074a)

## Authentication in App registration
## ![image](https://github.com/user-attachments/assets/8f0206c7-c4ed-49f6-8042-d312c30f9932)

## Create Secret
![image](https://github.com/user-attachments/assets/94c18de2-a448-4d47-b732-4d2ed75246e7)

## Token Configuration.
![image](https://github.com/user-attachments/assets/502b2cc1-6c85-48af-9fb1-0f1a00be58db)

## API Permissions
![image](https://github.com/user-attachments/assets/bd89eb72-b859-4153-a697-d1420c6c575c)

## Configuration in the server
```
root# cat /etc/systemd/system/PConnect.service
[Unit]
Description=Start PConnection App

[Service]
Type=forking
WorkingDirectory=/data/app
ExecStart=/usr/local/bin/PConnection.sh

[Install]
WantedBy=multi-user.target
```
```
#==========================================
root# cat 
#!/usr/bin/env bash
source bin/activate
nohup /data/chop/bin/python3.10 PConnect/bin/manage.py runserver  &
#===========================================
```
## Settings.py
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

AUTHENTICATION_BACKENDS = [

    'django_auth_adfs.backend.AdfsAccessTokenBackend',

]


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

    
LOGIN_URL = "django_auth_adfs:login"
LOGIN_REDIRECT_URL = "/"
```
## urls.py.
```
from django.conf.urls import include
urlpatterns = [
    ...
    path('oauth2/', include('django_auth_adfs.urls')),
    ...
]
```

