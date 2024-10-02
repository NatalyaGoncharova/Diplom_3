import requests
from data import *
from faker import Faker

fake = Faker()


class UserAuthorisation:
    @staticmethod
    def registrate_user(email, password, name):
        url = REGISTRATE_API_URL
        data = {"email": email, "password": password, "name": name}
        response = requests.post(url, json=data)
        return response

    @staticmethod
    def delete_user(access_token):
        url = DELETE_API_URL
        header = {'Authorization': f'Bearer {access_token}'}
        requests.delete(url, headers=header)









