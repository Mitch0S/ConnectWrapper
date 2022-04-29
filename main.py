"""
Active Token: 358c738f-8b0a-4b26-85bf-6f5bca24bbc9
Expired Token: 55d3d40a-277a-4a69-861d-e2f90144cc62

Current Wrapper Functions:
  Auth:
    - Get Access Token
    - Check Access Token
    
  Notice:
    - Get Feed
    - Add Comment
    - View Notice

"""

"Auth Wrapper Functions"
# request = ConnectWrapper.Mobile.Auth().get_access_token(username="mitch.naake", password="Password1*")
# request = ConnectWrapper.Mobile.Auth().check_access_token(token="c276ac5d-9e27-4077-b7c2-6fa38d0fa134")

"Notice Wrapper Functions"
# request = ConnectWrapper.Mobile.Notices().get_feed(token="358c738f-8b0a-4b26-85bf-6f5bca24bbc9", size=25)
# request = ConnectWrapper.Mobile.Notices().add_comment(token='358c738f-8b0a-4b26-85bf-6f5bca24bbc9', message_id='Message:3888078839', comment="If you see this, my wrapper for adding comment worked!")
# request = ConnectWrapper.Mobile.Notices().view_notice(token='358c738f-8b0a-4b26-85bf-6f5bca24bbc9', item_event='ItemEvent:3995858482')

'''
pypi-AgEIcHlwaS5vcmcCJGY1ODU2N2Y5LWU2N2UtNDJkNi04Y2ZjLWRiN2NiOThkMzI4OQACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgF8KZEmsETyFz7q1c7wEj6RbXzivqvsnddgQhig5ssQE
'''