import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='db_test_queue')


channel.basic_publish(exchange='', routing_key='db_test_queue', body='DATABASE CHECK')
print("Sending Message -->> 'CHECKING DB CONNECTION!'")
connection.close()