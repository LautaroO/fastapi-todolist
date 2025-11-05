from fastapi.security import OAuth2AuthorizationCodeBearer

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="http://localhost:8080/realms/todoapp/protocol/openid-connect/auth",
    tokenUrl="http://localhost:8080/realms/todoapp/protocol/openid-connect/token",
    refreshUrl="http://localhost:8080/realms/todoapp/protocol/openid-connect/token",
)
