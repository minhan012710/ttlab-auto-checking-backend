from fastapi.security import OAuth2PasswordBearer
from configparser import ConfigParser
import http.client
import jwt
import json
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_token(config):
    """generate auth0 token"""

    # conn = http.client.HTTPSConnection(config['DOMAIN'])
    conn = http.client.HTTPSConnection("dev-faxkci95.jp.auth0.com")
    '''
    payload = {
        "client_id": config['CLIENT_ID'],
        "client_secret": config['SECRET_KEY'],
        "audience": config['API_AUDIENCE'],
        "grant_type": "client_credentials"
    }
    '''
    payload = {
        "client secret": "kqVvfaLrgxvg2G7ijMs8nAH1hlwDapm-3FnxABU_4iZZTiRckpv1HX--HVeAGaQb",
        "client id": "ouULJEOJ4xOMrEpGztVlXMGnEjGD5Hn3",
        "audience": "",
        "grant_type": "client_credentials"
    }
    payload = json.dumps(payload).replace(" ", "")
    
    headers = { 'content-type': "application/json" }
    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    return str(json.loads(data.decode("utf-8"))['access_token'])

def set_up():
    """set up configuration"""

    env = os.getenv("APP_NAME")
    config = ConfigParser()
    config.read(".env")
    app_config = {
        "APP_NAME": config["app"]["APP_NAME"],
        "ORIGINS": config["app"]["ORIGINS"],
        "HEADERS": config["app"]["HEADERS"],
        "METHODS": config["app"]["METHODS"],
        "CREDENTIALS": True,
        "TIMS_URL": config["tims"]["TIMS_URL"],
        "DOMAIN": config["auth"]["DOMAIN"],""
        "API_AUDIENCE": config["auth"]["API_AUDIENCE"],
        "ISSUER": config["auth"]["ISSUER"],
        "ALGORITHMS": config["auth"]["ALGORITHMS"],
        "CLIENT_ID": config["auth"]["CLIENT_ID"],
        "SECRET_KEY": config["auth"]["SECRET_KEY"]
    }
    return app_config

config = set_up()

print(get_token(config))

class VerifyToken():
    """token verification using PyJWT"""

    def __init__(self, token, permissions=None, scopes=None):
        self.token = token
        self.permissions = permissions
        self.scopes = scopes
        self.config = set_up()
        jwks_url = f'https://{config["DOMAIN"]}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    def verify(self):
        try:
            self.signing_key = self.jwks_client.get_signing_key_from_jwt(
                self.token
            ).key
        except jwt.exceptions.PyJWKClientError as error:
            return {"status": "error", "msg": error.__str__()}
        except jwt.exceptions.DecodeError as error:
            return {"status": "error", "msg": error.__str__()}

        try: 
            payload = jwt.decode(
                self.token,
                self.signing_key,
                algorithms = config["ALGORITHMS"],
                audience = config["API_AUDIENCE"],
                issuer = config["ISSUER"],
            )
        except Exception as e:
            return {"status": "error", "message": str(e)}

        if self.scopes:
            result = self._check_claims(payload, 'scope', str, self.scopes.split(' '))
            if result.get("error"):
                return result

        if self.permissions:
            result = self._check_claims(payload, 'permissions', list, self.permissions)
            if result.get("error"):
                return result

        return payload

    def _check_claims(self, payload, claim_name, claim_type, expected_value):

        instance_check = isinstance(payload[claim_name], claim_type)
        result = {"status": "success", "status_code": 200}

        payload_claim = payload[claim_name]

        if claim_name not in payload or not instance_check:
            result["status"] = "error"
            result["status_code"] = 400

            result["code"] = f"missing_{claim_name}"
            result["msg"] = f"No claim '{claim_name}' found in token."
            return result

        if claim_name == 'scope':
            payload_claim = payload[claim_name].split(' ')

        for value in expected_value:
            if value not in payload_claim:
                result["status"] = "error"
                result["status_code"] = 403

                result["code"] = f"insufficient_{claim_name}"
                result["msg"] = (f"Insufficient {claim_name} ({value}). You "
                                  "don't have access to this resource")
                return result
        return result