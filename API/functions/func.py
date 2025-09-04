from DataBase.models import Users
from ..users_route import pydantic_models as pd_md

class Functions_API:

    @staticmethod
    def convert_list_users(lst: list[Users]) -> pd_md.User:
        new_list = []
        for elem in lst:
            new_list.append(pd_md.User(**elem.__dict__))
        
        return new_list

