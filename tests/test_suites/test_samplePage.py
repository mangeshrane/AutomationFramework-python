'''
Created on Feb 7, 2019

@author: mrane
'''
 
from core.api.request import ContentType, Request
 
headers = {
   'cache-control': "no-cache",
   'postman-token': "7f2e23ce-9c42-5184-6249-1a2031d95f45"
   }

response = Request().header(ContentType.URLENC).set_base_url("https://postman-echo.com/post").add_param("strange", "boom").add_headers(headers
                                                                                                                     ).post("post")
# response.assert_response_code(200).body().assert_equals("page", [1, 2])
print(type(response.body))
print(response.body)


