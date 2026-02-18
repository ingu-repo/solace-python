# Solace
Testing Solace Pub/Sub model as well as Que model by Python.

# Pub/Sub Model
Pubslishing messages to Topic is volatile, it means the published messages disappear if Subscribers didn't receive at that time.
It is broadcast model that you can receive if you are interested in them such as sports playing / market prices / etc

# Que Model
Publishing messages to Queue is kept until Subscriber deletes them.

# Environments
Using docker for Solace service.

### INSTALL & RUN
    docker run -d -p 8080:8080 -p 55554:55555 -p 8008:8008 --shm-size=2g --env username_admin_globalaccesslevel=admin --env username_admin_password=admin --name=solace solace/solace-pubsub-standard:latest

### CHECK SERVICE
http://localhost:8080 
(Login: admin / admin)

### USEFUL DOCKER COMMANDS
    docker ps
    docker stop solace
    docker start solace
    docker logs -f solace

### INTERACTIVE MODE
    docker exec -it solace /usr/sw/loads/currentload/bin/cli -A

### Python to use Solace
    pip install solace-pubsubplus



