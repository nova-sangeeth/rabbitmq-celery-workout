import pika, sys, os
# from db_conn import connection_test
from db_backup_methods import  backup_postgres_db
import datetime


connection = pika.BlockingConnection(pika.ConnectionParameters(host="dev.screel.in"))
channel = connection.channel()

channel.queue_declare(queue="db_backup_test_queue")
channel.queue_declare(queue="db_test_queue")

time = datetime.datetime.now()


def callback(ch, method, properties, body):
    backup_postgres_db(
        database_name="app",
        dest_file=f'test_{time}.sql', 
        host='dev.screel.in', 
        password='postgres', 
        port=6432, 
        user= 'postgres',
        table_only=True
    )
    print(" [x] Received %r" % body)

def db_connection_check(ch, method, properties, body):
    # connection_test()
    print('DB is now functional')
    print(" [x] Received %r" % body)

    

channel.basic_consume(queue="db_backup_test_queue", on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue="db_test_queue", on_message_callback=db_connection_check, auto_ack=True)
print(" [*] Waiting for trigger.")
channel.start_consuming()
