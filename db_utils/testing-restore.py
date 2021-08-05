from os import path
import wget
import subprocess
import logging
import datetime
import requests
import tempfile
import urllib
logger = logging.getLogger(__name__)

import os



def restore_postgres_db(db_host, db, port, user, password, backup_file):
    try:
        print(user,password,db_host,port, db)
        process = subprocess.Popen(
            [
                'pg_restore',
                '--verbose',
                '--clean',
                '--dbname=postgresql://{}:{}@{}:{}/{}'.format(user, password, db_host, port, db),
                backup_file
            ],
            stdout=subprocess.PIPE
        )
        output = process.communicate()[0]
        if int(process.returncode) != 0:
            print('Command failed. Return code : {}'.format(process.returncode))

        return output
    except Exception as e:
        print("Issue with the db restore : {}".format(e))


def restore_reference_data():
    try:
        backup_file_path = "dump.sql"
        logger.debug('Temporary file path ==>' + backup_file_path)
    
    except Exception as e:
        logger.warning("Issue with retreiving the link : {}".format(e))
    
    try:
        restore_postgres_db(
            db_host = 'db',
            db = 'app', 
            port = 5432, 
            user = 'postgres', 
            password = 'postgres', 
            backup_file = backup_file_path
        )
        os.remove(backup_file_path)
        print('removing temp file.....')
        return 'DB restore done!!'

    except Exception as e:
            logger.warning("Issue with the db restore : {}".format(e))
            return 'DB restore failed!!'


def concat_sqlfiles(file_path):
    try:
        process = subprocess.Popen(
            [
                        
            ],
            stdout=subprocess.PIPE
        )
        output = process.communicate()[0]
        if int(process.returncode) != 0:
            print('Command failed. Return code : {}'.format(process.returncode))

        print('Successfully Completed')
    except:
        print('Error Unable to concat')
    return None