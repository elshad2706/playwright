# def test_inventory(page):
#     response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
#     print("status ==", response.status)
#     print("Response", response.json())
#     print("text", response.text())
#     print("body", response.body())


# def test_add_user(page):
#     data = [
#         {
#             "id": 9743,
#             "username": "fsd",
#             "firstName": "fff",
#             "lastName": "ggg",
#             "email": "bbb",
#             "password": "tt",
#             "phone": "333",
#             "userStatus": 0
#         }
#     ]
#     header = {
#         'accept': 'application/json',
#         'content-Type': 'application/json'
#     }
#     response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray', data=data, headers=header)
#     print(response.status)
#     print(response.text())
#     print(response.json())
#     print(response.body())


def test_inventory(page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    assert response.status == 200

    print(response.status)
    print(response.json()["sold"])
