import time
import os
import subprocess

db_creds = {
    "server": "localhost",
    "port": 5432,
    "driver": "PostgreSQL",
    "database": "app",
    "username": "postgres",
    "password": "postgres",
}


tables_list = [
    "action_types",
    "actions",
    "benefit_types",
    "candidate_levels",
    "candidate_types",
    "contact_types",
    "country_info",
    "currencies",
    "customer_type",
    "customer_user_types",
    "display_types",
    "display_data",
    "districts",
    "document_ext",
    "document_owner",
    "document_types",
    "document_type_ext",
    "gender",
    "issue_authorities",
    "issue_authority_candidate_type",
    "issue_authority_qual",
    "issue_authority_type",
    "job_candidate_process",
    "job_candidate_process_action",
    "job_candidate_process_actions",
    "language_proficiency",
    "languages",
    "locations",
    "marital_status",
    "non_medical_qual_type",
    "non_medical_qual",
    "organisation_types",
    "pqr_header",
    "pqr_detail",
    "pqr_ahp_detail",
    "qualification_classification",
    "qualifications",
    "reason_types",
    "reasons",
    "recruitment_types",
    "region_countries",
    "regions",
    "role_types",
    "skill_types",
    "skills",
    "special_interest",
    "speciality",
    "sub_speciality",
    "speciality_types",
    "speciality_sub_speciality_self_reference_types",
    "speciality_sub_speciality_self_references",
    "status",
    "status_types",
    "speciality_lookup",
    "keyword_most_frequent_word",
    "tabs",
    "team_levels",
    "titles",
    "filters",
    "entities",
    "departments",
    "divergents",
    "customer_admin_types",
    "job_detail_type",
    "job_types",
]


def backup_postgres_db(
    host, database_name, port, user, password, dest_file, table_only
):
    """
    Backup postgres db to a file.
    """
    reference_tables = " ".join([f'--table={e.strip()}' for e in tables_list])
    # print(reference_tables)
    if table_only:
        try:
            process = subprocess.Popen(
                [
                    "pg_dump",
                    "--data-only",
                    "--exclude-table-data=ab_*",

                    "--table=action_types",
                    "--table=actions",
                    "--table=benefit_types",
                    "--table=candidate_levels",
                    "--table=candidate_types",
                    "--table=contact_types",
                    "--table=country_info",
                    "--table=currencies",
                    "--table=customer_type",
                    "--table=customer_user_types",
                    "--table=display_types",
                    "--table=display_data",
                    "--table=districts",
                    "--table=document_ext",
                    "--table=document_owner",
                    "--table=document_types",
                    "--table=document_type_ext",
                    "--table=gender",
                    "--table=issue_authorities",
                    "--table=issue_authority_candidate_type",
                    "--table=issue_authority_qual",
                    "--table=issue_authority_type",
                    "--table=job_candidate_process",
                    "--table=job_candidate_process_action",
                    "--table=job_candidate_process_actions",
                    "--table=language_proficiency",
                    "--table=languages",
                    "--table=locations",
                    "--table=marital_status",
                    "--table=non_medical_qual_type",
                    "--table=non_medical_qual",
                    "--table=organisation_types",
                    "--table=pqr_header",
                    "--table=pqr_detail",
                    "--table=pqr_ahp_detail",
                    "--table=qualification_classification",
                    "--table=qualifications",
                    "--table=reason_types",
                    "--table=reasons",
                    "--table=recruitment_types",
                    "--table=region_countries",
                    "--table=regions",
                    "--table=role_types",
                    "--table=skill_types",
                    "--table=skills",
                    "--table=special_interest",
                    "--table=speciality",
                    "--table=sub_speciality",
                    "--table=speciality_types",
                    "--table=speciality_sub_speciality_self_reference_types",
                    "--table=speciality_sub_speciality_self_references",
                    "--table=status",
                    "--table=status_types",
                    "--table=speciality_lookup",
                    "--table=keyword_most_frequent_word",
                    "--table=tabs",
                    "--table=team_levels",
                    "--table=titles",
                    "--table=filters",
                    "--table=entities",
                    "--table=departments",
                    "--table=divergents",
                    "--table=customer_admin_types",
                    "--table=job_detail_type",
                    "--table=job_types",
                    
                    "--dbname=postgresql://{}:{}@{}:{}/{}".format(user, password, host, port, database_name),
                    "-f",
                    dest_file,
                    "-v",
                ],
                stdout=subprocess.PIPE,
            )
            output = process.communicate()[0]
            if int(process.returncode) != 0:
                print("Command failed. Return code : {}".format(process.returncode))
                exit(1)
            return output
        except Exception as e:
            print(e)
            exit(1)
    else:

        try:
            process = subprocess.Popen(
                [
                    "pg_dump",
                    "--dbname=postgresql://{}:{}@{}:{}/{}".format(user, password, host, port, database_name),
                    "-f",
                    dest_file,
                ],
                stdout=subprocess.PIPE,
            )
            output = process.communicate()[0]
            if process.returncode != 0:
                print("Command failed. Return code : {}".format(process.returncode))
                exit(1)
            return output
        except Exception as e:
            print(e)
            exit(1)
