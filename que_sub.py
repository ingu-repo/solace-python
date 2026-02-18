import time
from solace.messaging.messaging_service import MessagingService
from solace.messaging.resources.queue import Queue
from solace.messaging.receiver.message_receiver import MessageHandler

class MyMessageHandler(MessageHandler):
    def __init__(self, receiver):
        self.receiver = receiver

    def on_message(self, message):
        try:
            payload = message.get_payload_as_string()
            print(f"Received: {payload}")

            # Delete Que messages
            self.receiver.ack(message)
        except Exception as e:
            print(f"exception: {e}")

config = {
    "solace.messaging.transport.host": "tcp://localhost:55554",
    "solace.messaging.service.vpn-name": "default",
    "solace.messaging.authentication.scheme.basic.username": "admin",
    "solace.messaging.authentication.scheme.basic.password": "admin"
}

messaging_service = MessagingService.builder().from_properties(config).build()
messaging_service.connect()

# Create Que
target_que = Queue.durable_exclusive_queue("first_test_que")

# Receiver
receiver = messaging_service.create_persistent_message_receiver_builder().build(target_que)
receiver.start()

# Subscribe
my_handler = MyMessageHandler(receiver)
receiver.receive_async(my_handler)

print ("Starting to receive que messages. Please Ctlr+C to stop")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    receiver.terminate()
    messaging_service.disconnect()






