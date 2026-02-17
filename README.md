Testing Solace Pub/Sub models in Python.
Using docker for Solace service.

# INSTALL & RUN
    docker run -d -p 8080:8080 -p 55554:55555 -p 8008:8008 --shm-size=2g --env username_admin_globalaccesslevel=admin --env username_admin_password=admin --name=solace solace/solace-pubsub-standard:latest

# CHECK SERVICE
http://localhost:8080 
(Login: admin / admin)

# USEFUL DOCKER COMMANDS
    docker ps
    docker stop solace
    docker start solace
    docker logs -f solace

# INTERACTIVE MODE
    docker exec -it solace /usr/sw/loads/currentload/bin/cli -A

# Python to use Solace
    pip install solace-pubsubplus



