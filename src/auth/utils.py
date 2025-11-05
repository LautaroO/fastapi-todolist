from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from typing import Annotated, List
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

def extract_roles_from_token(payload: dict, client_id: str) -> set[str]:
    roles = set()

    # roles de realm
    realm_roles = payload.get("realm_access", {}).get("roles", [])
    roles.update(realm_roles)

    # roles del cliente (resource_access)
    client_roles = (
        payload.get("resource_access", {})
        .get(client_id, {})
        .get("roles", [])
    )
    roles.update(client_roles)

    return roles

def require_roles(required_roles: List[str]):
    def dependency(payload: dict = Depends(valid_access_token)):
        user_roles = extract_roles_from_token(payload, client_id="todo-app")

        # ¿tiene al menos uno de los roles requeridos?
        if not any(role in user_roles for role in required_roles):
            raise HTTPException(
                status_code=403,
                detail="Not enough permissions",
            )
        return payload  # por si el endpoint quiere usar los claims
    return dependency