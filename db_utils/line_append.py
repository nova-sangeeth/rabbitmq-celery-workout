import os

def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.sql','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.sql',originalfile)


insert('ref_data_2.sql', 'SET session_replication_role to replica; DROP SCHEMA  IF EXISTS reference_data;')