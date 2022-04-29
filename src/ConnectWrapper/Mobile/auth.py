import traceback
import random
import requests
import base64

class Auth:
    def get_access_token(self, **kwargs):
        """
        Mobile.Auth.get_access_token

        get_access_token is used to retrieve a session token from the ConnectNow API server

        kwargs:
          `username` : string : N/A char : Alphanumeric, must contain `.` in middle
          `password` : string : N/A char
        """
        required_kwargs = ['username', 'password']
        missing_required_kwargs = []
        for required_kwarg in required_kwargs:
            if required_kwarg not in kwargs:
                missing_required_kwargs.append(required_kwarg)
        if len(missing_required_kwargs) > 0:
            return {'status': 'error', 'reason': 'you are missing required kwargs', 'data': {'kwargs': {'required': required_kwargs, 'missing': missing_required_kwargs}}}

        # SENDING THE REQUEST TO RETRIEVE THE AUTH TOKEN
        try:
            url = "https://connect.det.wa.edu.au/mobile/oauth/token"
            headers = {
                "Authorization": f"Basic {base64.b64encode(b'connect-mobile:7df5336c-3634-4a64-bd0d-7f0d504d7eaf').decode()}"
            }
            url_data = f"?username={kwargs['username']}&password={kwargs['password']}&grant_type=password&scope=connectNow"

            response = requests.post(url + url_data, headers=headers)
            if 'error' in response.json():
                return {'status': 'error', 'reason': (response.json()['error_description']).lower()}

            if 'access_token' in response.json():
                return {'status': 'ok', 'reason': 'successfully retrieved access token', 'data': {
                    'access_token': response.json()['access_token'],
                    'expires_in': response.json()['expires_in']
                }}
        except Exception as error:
            traceback.print_exc()
            return {'status': 'error', 'reason': error}


    def check_access_token(self, **kwargs):
        """
        Mobile.Auth.check_access_token

        check_access_token is used to check if a session token is still valid with ConnectNow API server

        kwargs:
          `token` : string : 36 char (4x'-', 32x'a-z0-9') Example: "55d3d40a-277a-4a69-861d-e2f90144cc62"
        """
        required_kwargs = ['token']
        missing_required_kwargs = []
        for required_kwarg in required_kwargs:
            if required_kwarg not in kwargs:
                missing_required_kwargs.append(required_kwarg)
        if len(missing_required_kwargs) > 0:
            return {'status': 'error', 'reason': 'you are missing required kwargs', 'data': {'kwargs': {'required': required_kwargs, 'missing': missing_required_kwargs}}}

        # SENDING THE REQUEST TO RETRIEVE THE AUTH TOKEN
        try:
            url = f"https://connect.det.wa.edu.au/mobile/api/v1/auth?context=connectnow&_dc={random.randint(1000000000000, 9999999999999)}"
            headers = {
                'Authorization': f'bearer {kwargs["token"]}'
            }
            response = requests.get(url, headers=headers)

            if 'error' in response.json():
                return {'status': 'error', 'reason': (response.json()['error_description'].lower()).split(":")[0]}

            if 'authorised' in response.json():
                return {'status': 'ok', 'reason': 'token is active', 'data': {'user': {'id': response.json()['user']['id'], 'type': response.json()['user']['primaryRole'], 'firstname': response.json()['user']['firstName'], 'lastname': response.json()['user']['lastName'], 'fullname': response.json()['user']['name'], 'username': response.json()['user']['screenName']}}}
        except Exception as error:
            traceback.print_exc()
            return {'status': 'error', 'reason': error}
