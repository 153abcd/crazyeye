# import requests
# import json
# a = {
#         "data": {
#             "project": {
#                 "url": "https: //www.teambition.com/project/596823f91f2d170ed3287f29/home",
#                 "_organizationId": "59682393361ddc461fa0f252",
#                 "_id": "596823f91f2d170ed3287f29",
#                 "name": "Issue管理"
#             },
#             "task": {
#                 "content": "FSA10001测试",
#                 "executor": {
#                     "_id": "596829cfe525d47670c4e479",
#                     "name": "冯超群",
#                     "avatarUrl": "https: //striker.teambition.net/thumbnail/110ud2216b9615c796999e437606a63f8033/w/200/h/200"
#                 },
#                 "_id": "5971cf438900c23e17cd3fcb"
#             },
#             "user": {
#                 "_id": "59682392e525d47670c4d49a",
#                 "name": "高飞",
#                 "avatarUrl": "https: //striker.teambition.net/thumbnail/110u54004f5d5582fc2e6eb7a08541f1573a/w/200/h/200"
#             }
#         },
#         "event": "task.remove"
#     }
# #方式一:
# headers = {"Content-Type":"application/json"}
# requests.post(url='http://127.0.0.1:8000/test.html',headers=headers,data=json.dumps(a))
#
# #方式二
# requests.post(url='http://127.0.0.1:8000/test.html',json=a)#只有body里有
# 生成器
# def countdown(count):
#     print("start")
#     while count > 0:
#         yield count
#         count -= 1
#     print("end")
# obj = countdown(5)
# while True:
#     try:
#         print(next(obj))
#     except Exception:
#         break

