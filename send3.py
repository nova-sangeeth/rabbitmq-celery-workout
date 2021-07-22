import pika
import json

from pika import channel


connection = pika.BlockingConnection(pika.ConnectionParameters("dev.screel.in"))
# Using for the local testing.
# connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))


channel = connection.channel()


channel.exchange_declare(exchange="testing_exchange", exchange_type="direct")


testing_information = {
    "user_email": "testerdude@gg.com",
    "address": "coonoor",
    "age": "100",
}

channel.basic_publish(
    exchange="testing_exchange",
    routing_key="testing_information.age",
    body=json.dumps({"user_email": testing_information["user_email"]}),
)


print("Sending the message from the binded queue!!")


connection.close()
