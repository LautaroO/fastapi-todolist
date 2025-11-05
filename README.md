

Keycloak:

Once container created, if https related errors, go to container terminal and:

cd /opt/keycloak/bin
./kcadm.sh config credentials --server http://localhost:8080 --realm master --user admin
./kcadm.sh update realms/master -s sslRequired=NONE

This will disable https for local developemnt purposes.

To request an access token for a user:

curl -X POST http://localhost:8080/realms/{REALM}/protocol/openid-connect/token -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=password" -d "client_id={clientId}" -d "username={user}" -d "password={password}";  

Replace curly braces variables ({variable}) with corresponding keycloak configurations

