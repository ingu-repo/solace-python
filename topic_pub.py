# Topic
#   - Published data is volatile
#
# Pre-requisites:
#   pip install solace-pubsubplus
#
# ---------------------------------------------------
import time
from datetime import datetime
from solace.messaging.messaging_service import MessagingService
from solace.messaging.resources.topic import Topic

# Connection configuration
solace_config = {
    "solace.messaging.transport.host": "tcp://localhost:55554",
    "solace.messaging.service.vpn-name": "default",
    "solace.messaging.authentication.scheme.basic.username": "admin",
    "solace.messaging.authentication.scheme.basic.password": "admin"
}

# Build and connect to the service
messaging_service = MessagingService.builder().from_properties(solace_config).build()
messaging_service.connect()

# Define topic and message
topic = Topic.of("seo/topic/first_test_topic")
publisher = messaging_service.create_direct_message_publisher_builder().build()
publisher.start()

# Publish messages
loop_count = 0
while True:
    if (loop_count > 2):
        break
    else:
        loop_count += 1

    curr_time = datetime.now().strftime("[%Y%m%d %H:%M:%S]")
    new_msg = f"{curr_time} hi there {loop_count}"
    message = messaging_service.message_builder().build(new_msg)
    publisher.publish(destination=topic, message=message)
    print(f"message published: {new_msg}")
    time.sleep(3)

publisher.terminate()
print("publisher terminated")

messaging_service.disconnect()
print("messaging service disconnected")

