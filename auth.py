import jwt
import base64
import logging
import logging
import requests
import urllib3
import json
import os
#     git_props["env_var"] = {var: os.environ.get(var) for var in env_var}


# from requests.adapters import HTTPAdapter, Retry
KEY = "hii"
logging.basicConfig(level=logging.ERROR)
# logging.getLogger("urllib3").setLevel(logging.WARNING)
s = requests.Session()

def replace_symbols(input: str) -> str:
    return input.replace("'", "") if input else input

if __name__ == '__main__':
    # auth_token = auth_token.split(" ")
    # base64_message = auth_token[1] if len(auth_token) > 1 else None 
    # token = ((base64.b64decode(base64_message)).decode('utf-8')).strip()
    # alg = jwt.get_unverified_header(token)['alg']
    # payload = jwt.decode(token, algorithms=[alg], options={"verify_signature": False})
    # print(payload['account_id_string'])
    url = 'http://127.0.0.1:8090/'
    data = {KEY: 'value'}
    print(data)

    data = {
        "final_report" : base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')
    }
    print(data)
    # try:
    #     retries = Retry(total=5, backoff_factor=1)
    #     s.mount('http://', HTTPAdapter(max_retries=retries))
    #     s.mount('https://', HTTPAdapter(max_retries=retries))
    #     s.post(url=url, json=data)
    # except urllib3.exceptions.NewConnectionError:
    #     print("connection failed")
    headers = {
        "content-type": "application/json",
        "Authorization": f"token",
        "CI": True,
    }
    """
    urllib3 will sleep for:
    {backoff factor} * (2 ** ({number of previous retries})) seconds
    """
    try:
        retries = urllib3.Retry(2, status_forcelist=[501], backoff_factor=10)
        http = urllib3.PoolManager(retries=retries)
        response = http.request("POST", url=url, json=data, headers=headers)
        print("report submitted", response.status)
    except urllib3.exceptions.LocationValueError as e:
        print(f'connection failed: {e}')
    # except ConnectionRefusedError as e:
    #     print("failed cr"),
    except urllib3.exceptions.NewConnectionError as e:
    #     print("failed nc")
        raise  urllib3.exceptions.MaxRetryError("This is max try erro") from e
        print("Connection Failed!")

    # di = dict()
    # try:
    #     # Attempt to retrieve the value of the environment variable
    #     env_var_value = os.environ.get("PR")
    #     di["p"] = env_var_value

    # except KeyError as e:
    #     print(f'Error: The en')
    # print(di)







