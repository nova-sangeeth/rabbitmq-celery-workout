import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='dev.screel.in'))
channel = connection.channel()

channel.queue_declare(queue='db_backup_test_queue')

channel.basic_publish(exchange='', routing_key='db_backup_test_queue', body='DATABASE CHECK')
print("Sending Message -->> 'DB BACKUP!'")


connection.close()