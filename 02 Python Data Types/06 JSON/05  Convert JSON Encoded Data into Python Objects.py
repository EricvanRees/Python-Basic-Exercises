"""
Write a Python program to convert JSON encoded data into Python objects.
"""

import json

json_obj = '{"id":1,"slug":"lorem-ipsum","url":"https://jsonplaceholder.org/posts/lorem-ipsum","title":"Lorem ipsum dolor sit amet, consectetur adipiscing elit.","content":"Ante taciti nulla sit libero orci sed nam. Sagittis suspendisse gravida ornare iaculis cras nullam varius ac ullamcorper. Nunc euismod hendrerit netus ligula aptent potenti. Aliquam volutpat nibh scelerisque at. Ipsum molestie phasellus euismod sagittis mauris, erat ut. Gravida morbi, sagittis blandit quis ipsum mi mus semper dictum amet himenaeos. Accumsan non congue praesent interdum habitasse turpis orci. Ante curabitur porttitor ullamcorper sagittis sem donec, inceptos cubilia venenatis ac. Augue fringilla sodales in ullamcorper enim curae; rutrum hac in sociis! Scelerisque integer varius et euismod aenean nulla. Quam habitasse risus nullam enim. Ultrices etiam viverra mattis aliquam? Consectetur velit vel volutpat eget curae;. Volutpat class mus elementum pulvinar! Nisi tincidunt volutpat consectetur. Primis morbi pulvinar est montes diam himenaeos duis elit est orci. Taciti sociis aptent venenatis dui malesuada dui justo faucibus primis consequat volutpat. Rhoncus ante purus eros nibh, id et hendrerit pellentesque scelerisque vehicula sollicitudin quam. Hac class vitae natoque tortor dolor dui praesent suspendisse. Vehicula euismod tincidunt odio platea aenean habitasse neque ad proin. Bibendum phasellus enim fames risus eget felis et sem fringilla etiam. Integer.","image":"https://dummyimage.com/800x430/FFFFFF/lorem-ipsum.png&text=jsonplaceholder.org","thumbnail":"https://dummyimage.com/200x200/FFFFFF/lorem-ipsum.png&text=jsonplaceholder.org","status":"published","category":"lorem","publishedAt":"04/02/2023 13:25:21","updatedAt":"14/03/2023 17:22:20","userId":1}'

python_objs = json.loads(json_obj)
for item, value in python_objs.items():
  print(item, value)

