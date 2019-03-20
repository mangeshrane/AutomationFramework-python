'''
Created on Feb 7, 2019

@author: mrane
'''

from core.api.request import ContentType, Request


response = Request().header(ContentType.JSON).set_base_url("https://reqres.in/").get("/api/users/2")
# response.assert_response_code(200).body().assert_equals("page", [1, 2])
print(type(response.body))
print(response.body)
print(response.body.data[0])

