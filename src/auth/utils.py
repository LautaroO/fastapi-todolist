from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from typing import Annotated
from jwt import PyJWKClient, decode

bearer_schema = HTTPBearer()
async def valid_access_token(
        credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer_schema)]
):
    url = "http://keycloak:8080/realms/todoapp/protocol/openid-connect/certs"
    jwks_client = PyJWKClient(url)
    
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(credentials.credentials)
        data = decode(
            credentials.credentials,
            signing_key.key,
            algorithms=["RS256"],
            audience=["todo-app"],
            options={"verify_exp": True},
        )
        return data
    except Exception as e:
        print(f"Token validation error: {e}")
        raise HTTPException(status_code=401, detail="Invalid access token") from e