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

download_link = 'https://talentfinddev.blob.core.windows.net/referencedata/data/data_backupreference_data_backup/ref_data_2021_08_01_19_09_23.sql'
print('file path for the reference data backup: ' + download_link)
r = requests.get(download_link, stream=True)
with open("dump.sql",'wb') as sql_dump_file:
    for chunk in r.iter_content(chunk_size=2048): # 2 mb chucks
        if chunk: 
            sql_dump_file.write(chunk)
backup_file_path = os.path.realpath(sql_dump_file.name)
print('file path' + backup_file_path)

# def restore_postgres_db(db_host, db, port, user, password, backup_file, verbose):
#     """
#     Restore postgres db from a file.
#     """

#     if verbose:
#         try:
#             print(user,password,db_host,port, db)
#             process = subprocess.Popen(
#                 [
#                     'pg_restore',
#                     '--verbose',
#                     '--clean',
#                     # '--data-only',
#                     '--dbname=postgresql://{}:{}@{}:{}/{}'.format(user, password, db_host, port, db),
#                     backup_file
#                 ],
#                 stdout=subprocess.PIPE
#             )
#             output = process.communicate()[0]
#             if int(process.returncode) != 0:
#                 print('Command failed. Return code : {}'.format(process.returncode))

#             return output
#         except Exception as e:
#             print("Issue with the db restore : {}".format(e))
#     else:
#         try:
#             process = subprocess.Popen(
#                 [
#                     'pg_restore', 
#                     '--verbose', 
#                     '--clean', 
#                     '--dbname=postgresql://{}:{}@{}:{}/{}'.format(user,password,db_host,port, db),
#                     backup_file
#                 ],
#                 stdout=subprocess.PIPE
#             )
#             output = process.communicate()[0]
#             if int(process.returncode) != 0:
#                 print('Command failed. Return code : {}'.format(process.returncode))

#             return output
#         except Exception as e:
#             print("Issue with the db restore : {}".format(e))


# def restore_reference_data():
#     try:
#         restore_postgres_db(
#             db_host="localhost",
#             db="app",
#             port=5432,
#             user="postgres",
#             password="postgres",
#             backup_file="./database-new.sql",
#             verbose=True
#         )
#     except Exception as e:
#         logger.warning("Issue with the db restore : {}".format(e))
#     return "DB restore done!!"


# restore_reference_data()
