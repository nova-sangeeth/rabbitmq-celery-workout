import psycopg2
import sys
import subprocess

conn = psycopg2.connect(
    database="app",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)


def connection_test():
    cursor = conn.cursor()

    cursor.execute("select version()")

    data = cursor.fetchone()
    print("Connection established to: ", data)

    # Closing the connection
    conn.close()
    # Connection established to: ('PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',)




        
def data_backup_testing():
   connection = conn
   try:
       cur = connection.cursor()
       cur.execute('SELECT x FROM t')
       f = open('test.sql', 'w')
       for row in cur:
         f.write("insert into t values (" + str(row) + ");")
   except psycopg2.DatabaseError:
       print ('ISSUES WITH BACKING UP THE DATA.')
       sys.exit(1)
   finally:
       if connection:
           connection.close()




def get_reference_data():
    tables = ["action_types",
              "actions", "benefit_types", "candidate_levels", "candidate_types", "contact_types", "country_info",
              "currencies", "customer_type",
              "customer_user_types", "display_types", "display_data", "districts", "document_ext", "document_owner",
              "document_types",
              "document_type_ext", "gender", "issue_authorities", "issue_authority_candidate_type",
              "issue_authority_qual", "issue_authority_type",
              "job_candidate_process", "job_candidate_process_action", "job_candidate_process_actions",
              "language_proficiency", "languages",
              "locations", "marital_status", "non_medical_qual_type", "non_medical_qual", "organisation_types",
              "pqr_header", "pqr_detail", "pqr_ahp_detail", 
              "qualification_classification", "qualifications", "reason_types", "reasons", "recruitment_types",
              "region_countries",
              "regions", "role_types", "skill_types", "skills", "special_interest", "speciality", "sub_speciality",
              "speciality_types",
              "speciality_sub_speciality_self_reference_types", "speciality_sub_speciality_self_references", "status",
              "status_types", "speciality_lookup", "keyword_most_frequent_word",  
              "tabs", "team_levels", "titles", "filters", "entities", "departments", 
              "divergents", "customer_admin_types", "job_detail_type", "job_types"]
    reference_tables = " ".join([f"-t public.{e}" for e in tables])
    cmd = "pg_dump {0} --data-only --exclude-table-data=ab_* {1} > app_reference_data_export.sql".format(
        conn, reference_tables)
    p = subprocess.call(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    if p:
       return f'work done///'




