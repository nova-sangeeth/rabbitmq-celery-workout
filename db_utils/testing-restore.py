from os import path
import wget
import subprocess
import logging
import datetime
import requests
import tempfile
import urllib
logger = logging.getLogger(__name__)

path = "https://talentfinddev.blob.core.windows.net/referencedata/data%2Fdata_backup%2Freference_data_backup%2Fref_data_2021_07_31_15_45_33.sql"

file_name = urllib.request.urlretrieve(url= path, filename="dump.sql")



def restore_postgres_db(db_host, db, port, user, password, backup_file, verbose):
    """
    Restore postgres db from a file.
    """

    if verbose:
        try:
            print(user,password,db_host,port, db)
            process = subprocess.Popen(
                [
                    'pg_restore',
                    '--clean',
                    '--dbname=postgresql://{}:{}@{}:{}/{}'.format(user, password, db_host, port, db),
                    '-v', 
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
    else:
        try:
            process = subprocess.Popen(
                [
                    'pg_restore', 
                    '--verbose', 
                    '--clean', 
                    '--dbname=postgresql://{}:{}@{}:{}/{}'.format(user,password,db_host,port, db),
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
        restore_postgres_db(
            db_host="localhost",
            db="app",
            port=5432,
            user="postgres",
            password="postgres",
            backup_file="./dump.sql",
            verbose=True
        )
    except Exception as e:
        logger.warning("Issue with the db restore : {}".format(e))
    return "DB restore done!!"


restore_reference_data()
