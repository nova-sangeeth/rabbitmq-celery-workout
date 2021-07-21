import pika, sys, os
from db_conn import connection_test
from db_backup_methods import  backup_postgres_db
import datetime
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")

time = datetime.datetime.now()


def callback(ch, method, properties, body):
    # connection_test()
    backup_postgres_db(
        database_name="app",
        dest_file=f'test_{time}.sql', 
        host='localhost', 
        password='postgres', 
        port=5432, 
        user= 'postgres',
        table_only=True
    )
    print(" [x] Received %r" % body)


channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
print(" [*] Waiting for trigger.")
channel.start_consuming()
