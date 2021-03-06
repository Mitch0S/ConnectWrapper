# ConnectWrapper
Written by Mitch Naake (Year 11 ATAR Computer Science, Butler College)

### _What is ConnectWrapper?_  
ConnectWrapper is an easy way for Western-Australian students to create their own apps around the teacher-student communication platform, https://connect.det.wa.edu.au/  


### _What are the benefits?_
ConnectWrapper handles all requests and responses to and from the Connect webserver. Responses from the webserver are parsed and compiled in a way that makes it easier to get information from your request, saving you endless time with trying to find specific data from your own request, it's all there in front of you, in an easy-to-read format!  


### _What can I do with ConnectWrapper?_
Upon it's initial release, ConnectWrapper has the following functions:

- Mobile
  - Authentication
    - `get_access_token` (Used for authenticating future requests)
    - `check_access_token` (Used to check whether an `access_token` is valid/invalid/expired)
    
  - Notices
    - `get_feed` (Returns posts depending on user's kwargs, default returns the 10 most-recent posts)
    - `view_notice` (Used to view the details about the notice, adds a view to notice view counter)
    - `add_comment` (Posts a comment to the specified `notice`)

*Please Note: There are more functions coming soon...*
