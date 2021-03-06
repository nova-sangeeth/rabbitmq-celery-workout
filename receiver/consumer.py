import pika
import json
import datetime

# from db_utils.db_backup_methods import  backup_postgres_db



credentials = pika.PlainCredentials('tester_1', 'tester')
# parameters = pika.ConnectionParameters('139.59.92.85',
parameters = pika.ConnectionParameters('40.123.213.154',
# parameters = pika.ConnectionParameters('40.123.215.82',
                                   5671,
                                   '/',
                                   credentials)
connection = pika.BlockingConnection(parameters)
# For local testing only
# connection = pika.Blockingconnection(pika.ConnectionParameters('localhost'))

time = datetime.datetime.now()

channel = connection.channel()

queue = channel.queue_declare('testing_q')
queue_name = queue.method.queue


# channel.queue_bind(
#     exchange='testing_exchange',
#     queue=queue_name,
#     routing_key='testing_information.age'
# )



def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(payload)
    # backup_postgres_db(
    #     database_name="app",
    #     dest_file=f'test_{time}.sql', 
    #     host='dev.screel.in', 
    #     password='postgres', 
    #     port=6432, 
    #     user= 'postgres',
    #     table_only=True
    # )
    print('COMPLETED!!!')
    ch.basic_ack(delivery_tag=method.delivery_tag)



channel.basic_consume(on_message_callback=callback,queue=queue_name)

print('waiting for any input from the user!!!')


channel.start_consuming()




def rabbit_start():
    connection = pika.BlockingConnection(pika.ConnectionParameters('tfdev.screel.in'))
    channel = connection.channel()
    queue = channel.queue_declare('testing_q')
    queue_name = queue.method.queue
    channel.queue_bind(exchange='testing_exchange', queue=queue_name, routing_key='testing_information.age')
    def callback(ch, method, properties, body):
        print(body)
        # backup_postgres_db(
        #     database_name="app",
        #     dest_file=f'test_{time}.sql',
        #     host='dev.screel.in',
        #     password='postgres',
        #     port=6432,
        #     user= 'postgres',
        #     table_only=True
        # )
        print('COMPLETED!!!')
        ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_consume(on_message_callback=callback, queue=queue_name)
    print('waiting for any input from the user!!!')
    channel.start_consuming()



rabbit_start()