"""
Current Wrapper Functions:
    Mobile:
      Auth:
        - Get Access Token
        - Check Access Token
    
    Notice:
      - Get Feed
      - Add Comment
      - View Notice
"""


#
#   MOBILE WRAPPER FUNCTIONS
#

"Auth Wrapper Functions"
# request = ConnectWrapper.Mobile.Auth().get_access_token(username="firstname.lastname", password="Password1***")
# request = ConnectWrapper.Mobile.Auth().check_access_token(token="c276ac5d-9e27-4077-b7c2-6fa38d0fa134")

"Notice Wrapper Functions"
# request = ConnectWrapper.Mobile.Notices().get_feed(token="c276ac5d-9e27-4077-b7c2-6fa38d0fa134", size=25)
# request = ConnectWrapper.Mobile.Notices().add_comment(token='c276ac5d-9e27-4077-b7c2-6fa38d0fa134', message_id='Message:1234567890', comment="If you see this, my wrapper for adding comment worked!")
# request = ConnectWrapper.Mobile.Notices().view_notice(token='c276ac5d-9e27-4077-b7c2-6fa38d0fa134', item_event='ItemEvent:1234567890')
