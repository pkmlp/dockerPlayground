
docker run -d --rm \
    --name MongoDB_Gui \
    --link MongoDB_Server:mongo \
    -p 8081:8081 \
    -e ME_CONFIG_MONGODB_SERVER="MongoDB_Server" \
    -e ME_CONFIG_MONGODB_ENABLE_ADMIN="false" \
    -e ME_CONFIG_MONGODB_AUTH_DATABASE="admin" \
    -e ME_CONFIG_MONGODB_AUTH_USERNAME="mongoAdmin" \
    -e ME_CONFIG_MONGODB_AUTH_PASSWORD="pkmlp" \
    mongo-express
