import traceback
import bs4
import requests
import random
import urllib.parse
import datetime
import json

class Notices:
    def get_feed(self, **kwargs):
        """
        Mobile.Notice.get_feed

        get_feed is used to retrieve a session token from the ConnectNow API server

        kwargs:
          `token` :  string : 36 char (4x'-', 32x'a-z0-9') : Example -> "55d3d40a-277a-4a69-861d-e2f90144cc62"
           `page` : integer : N/A char
           `size` : integer : N/A char


        Future updates:
            Enable a kwarg list to return the data that is wanted by the user
        """
        required_kwargs = ['token']
        missing_required_kwargs = []
        for required_kwarg in required_kwargs:
            if required_kwarg not in kwargs:
                missing_required_kwargs.append(required_kwarg)
        if len(missing_required_kwargs) > 0:
            return {'status': 'error', 'reason': 'you are missing required kwargs', 'data': {'kwargs': {'required': required_kwargs, 'missing': missing_required_kwargs}}}

        try:
            if 'size' in kwargs:
                size = int(kwargs['size'])
            else:
                size = 10
        except:
            size = 10

        try:
            if 'page' in kwargs:
                page = f"&page={int(kwargs['page'])}"
            else:
                page = ""
        except:
            page = ""

        try:
            url = f"https://connect.det.wa.edu.au/mobile/api/v1/stream/card?_dc={random.randint(1000000000000, 9999999999999)}&size={size}{page}"
            headers = {
                'Authorization': f'bearer {kwargs["token"]}'
            }
            response = requests.get(url, headers=headers)

            if 'error' in response.json():
                return {'status': 'error', 'reason': response.json()['error_description'].lower().split(":")[0]}

            if response.json() == {'success': True}:
                return {'status': 'error', 'reason': 'the specified size is too large, server responded none'}

            if 'success' in response.json():
                notices = response.json()['data']
                notice_list = []
                for notice in notices:
                    #print(json.dumps(notice, indent=2))
                    notice_list.append([{
                        'title': notice['data']['title'],
                        'class': notice['data']['owner']['name'],
                        'teacher': notice['data']['createdBy']['name'],
                        'event_item': notice['id'],
                        'notice_id': notice['data']['id'],
                        'comments_enabled': notice['data']['canRespond'],
                        'epoch_time': notice['eventDate']/1000,
                        'date_time': (datetime.datetime.fromtimestamp(notice['eventDate']/1000).strftime('%Y-%m-%d %H:%M:%S').split(" "))
                    }])
                return {'status': 'ok', 'reason': 'successfully retrieved notices', 'data': {'notices': notice_list}}

        except KeyError as error:
            traceback.print_exc()
            return {'status': 'error', 'reason': f'could not find {str(error).lower()} in response'}

        except Exception as error:
            traceback.print_exc()
            return {'status': 'error', 'reason': str(error)}



    def view_notice(self, **kwargs):
        """
        Mobile.Notice.view_notice

        get_session_token is used to retrieve a session token from the ConnectNow API server

        kwargs:
               `token` : string : 36 char (4x'-', 32x'a-z0-9')             : Example -> "55d3d40a-277a-4a69-861d-e2f90144cc62"
          `item_event` : string : 20 char (1x'ItemEvent', 1x':', 10x'0-9') : Example -> "ItemEvent:3828889073"
        """

        required_kwargs = ['token', 'item_event']
        missing_required_kwargs = []
        for required_kwarg in required_kwargs:
            if required_kwarg not in kwargs:
                missing_required_kwargs.append(required_kwarg)
        if len(missing_required_kwargs) > 0:
            return {'status': 'error', 'reason': 'you are missing required kwargs', 'data': {'kwargs': {'required': required_kwargs, 'missing': missing_required_kwargs}}}

        access_token = kwargs['token']
        ItemEvent = urllib.parse.quote(kwargs['item_event'])
        url = f"https://connect.det.wa.edu.au/mobile/api/v1/stream/card/{ItemEvent}?_dc={random.randint(1000000000000, 9999999999999)}"
        headers = {
            "Authorization": f"bearer {access_token}"
        }

        response = requests.get(url, headers=headers, timeout=5)

        if 'error' in response.json():
            return {'status': 'error', 'reason': response.json()['error_description'].lower().split(":")[0]}

        if response.json()['success'] == False:
            return {'status': 'error', 'reason': response.json()['message'].lower().split(":")[0]}

        if response.json()['success'] == True:
            notice = response.json()['data']
            return {'status': 'ok', 'reason': 'successfully retrieved notice', 'data': {
                'notice': {
                    'title': notice['data']['title'],
                    'content': {
                        'parsed': ' '.join(bs4.BeautifulSoup(notice['data']['content'], "html.parser").stripped_strings),
                        'raw': notice['data']['content']
                    },
                    #'class': notice['data']['name'],
                    'author': {
                        'name': notice['data']['createdBy']['name'],
                        'screen_name': notice['data']['createdBy']['screenName'],
                        'role': notice['data']['createdBy']['primaryRole']
                    },
                    'comments_enabled': notice['data']['canRespond'],
                    'item_event': notice['id'],
                    'message_id': notice['data']['id'],
                    'epoch_time': notice['eventDate']/1000,
                    'date_time': datetime.datetime.fromtimestamp(notice['eventDate']/1000).strftime('%Y-%m-%d %H:%M:%S').split(" ")

                }
            }}
        print(response.json())
        if 'error' in response.json():
            return {'status': 'error', 'reason': response.json()['error_description'].lower().split(":")[0]}


    def add_comment(self, **kwargs):
        """
        Mobile.Notice.add_comment

        get_session_token is used to retrieve a session token from the ConnectNow API server

        kwargs:
          `token` :  string : 36 char (4x'-', 32x'a-z0-9') : Example -> "55d3d40a-277a-4a69-861d-e2f90144cc62"
           `page` : integer : N/A char
           `size` : integer : N/A char
        """

        required_kwargs = ['token', 'message_id', 'comment']
        missing_required_kwargs = []
        for required_kwarg in required_kwargs:
            if required_kwarg not in kwargs:
                missing_required_kwargs.append(required_kwarg)
        if len(missing_required_kwargs) > 0:
            return {'status': 'error', 'reason': 'you are missing required kwargs', 'data': {'kwargs': {'required': required_kwargs, 'missing': missing_required_kwargs}}}

        try:
            url = f"https://connect.det.wa.edu.au/mobile/api/v1/action/comment/{kwargs['message_id']}?comment={urllib.parse.quote(kwargs['comment'])}"
            headers = {
                'Authorization': f'bearer {kwargs["token"]}'
            }
            response = requests.put(url, headers=headers)

            if response.json()['success'] == True:
                return {'status': 'ok', 'reason': 'successfully added comment', 'data': {
                    'message_id': kwargs['message_id'],
                    'comment': {
                        'raw': kwargs['comment'],
                        'url_encoded': urllib.parse.quote(kwargs['comment'])
                    }
                }}

            if response.json()['success'] == False:
                return {'status': 'error', 'reason': response.json()['message'].lower()}


        except KeyError as error:
            traceback.print_exc()
            return {'status': 'error', 'reason': f'could not find {str(error).lower()} in response'}

        except Exception as error:
            traceback.print_exc()
            return {'status': 'error', 'reason': str(error)}

