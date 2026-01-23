"""
Des outils pour l'EDS
"""
import requests
from functools import lru_cache
from pydantic import BaseModel
from os import getenv
import eds_routes
from eds_models import project
import os
import getpass


class TokenQueryParams(BaseModel):
    """ Informations de Token """
    username: str
    password: str
    grant_type: str = 'password'
    client_id: str = 'eds-public'


@lru_cache
def get_token():
    """
    Aller chercher un token EDS
    """

    username = os.getenv('NB_USER')
    
    @lru_cache
    def get_password():
        return getpass.getpass(f"password for {username}?")

    
    params = TokenQueryParams(username = username, password = get_password())
    resp = requests.post(url=eds_routes.TOKEN_URL, data=params.model_dump())
    try:
        token = resp.json()["access_token"]
    except KeyError:
        raise RuntimeError('Invalid username/password')

    return token


def req_with_token(method: str | bytes, url: str | bytes, schema: BaseModel | None = None, *args, **kwargs):
    """ Execute une requète avec un token"""
    headers: dict = kwargs.get('headers', {})
    headers.update({'Authorization': f"Bearer {get_token()}"})
    kwargs['headers'] = headers
    response = requests.request(method, url, *args, **kwargs)
    
    if response.status_code in [401, 403]:
        # Try to launch request again after updating token
        get_token.cache_clear()
        headers.update({'Authorization': f"Bearer {get_token()}"})
        kwargs['headers'] = headers

        response = requests.request(method, url, *args, **kwargs)

    if schema:
        json_data= response.json()
        print(list(json_data.keys()))
        response = schema.model_validate(json_data)
    return response


def list_user_projects():
    '''
    list user projects
    '''  
    url = eds_routes.PROJECTS['list']
    response: project.PageOfProjectDTO = req_with_token('get', url, schema=project.PageOfProjectDTO)
    response.
    return response


if __name__ == '__main__':
    print(list_user_projects())