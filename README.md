

Keycloak:

Once container created, go to container terminal and:

# cd /opt/keycloak/bin
# ./kcadm.sh config credentials --server http://localhost:8080 --realm master --user admin
# ./kcadm.sh update realms/master -s sslRequired=NONE

This will disable https for local developemnt purposes