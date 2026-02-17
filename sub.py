from solace.messaging.messaging_service import MessagingService
from solace.messaging.resources.topic_subscription import TopicSubscription
from solace.messaging.receiver.message_receiver import MessageHandler

class MessageHandlerImpl(MessageHandler):
    def on_message(self, message):
        print(f"Received message: {message.get_payload_as_string()}")

# Connection config. Same as publisher
solace_config = {
    "solace.messaging.transport.host": "tcp://localhost:55554",
    "solace.messaging.service.vpn-name": "default",
    "solace.messaging.authentication.scheme.basic.username": "admin",
    "solace.messaging.authentication.scheme.basic.password": "admin"
}

messaging_service = MessagingService.builder().from_properties(solace_config).build()
messaging_service.connect()

# Subscribe to the topic
topics = [TopicSubscription.of("seo/topic/first_test_topic")]
receiver = messaging_service.create_direct_message_receiver_builder().with_subscriptions(topics).build()
receiver.start()

# Set the callback handler
receiver.receive_async(MessageHandlerImpl())

print("Listening messages: press Ctrl+C to stop ...")
try:
    while True:
        pass
except KeyboardInterrupt:
    receiver.terminate()
    print("receiver terminated")

    messaging_service.disconnect()
    print("messaging service disconnected")









