from app.db.session import db_session

engine = db_session.bind


from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.inspection import inspect
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    text,
    ForeignKey,
    UniqueConstraint,
)
from fastapi.encoders import jsonable_encoder


def compile_query(query):
    compiler = (
        query.compile if not hasattr(query, "statement") else query.statement.compile
    )
    return compiler(dialect=postgresql.dialect())


def get_data_from_table(db_session, table_name: str):
    query = db_session.query(table_name).all()
    data = jsonable_encoder(query)
    return data


def get_primary_key_constraint(table_name: str):

    table_name = "contact_types"
    res = db_session.execute(
        f"""
            SELECT
                tc.constraint_name,
                tc.table_name,
                kcu.column_name,
                ccu.table_name AS foreign_table_name,
                ccu.column_name AS foreign_column_name
            FROM
                information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage AS ccu
                ON ccu.constraint_name = tc.constraint_name
                AND ccu.table_schema = tc.table_schema
            WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name='{table_name}';
                """
    )
    if res:
        p_key = list(res)[0][0]
        return p_key


def upsert(db_session, model, insert_data, constraint_name):
    """
    : param: insert_data:  must be a list of dictionary
    : param: model: SQLA Model Class
    : param: db_session: db_session
    """
    table = model.__table__

    statement = insert(table).values(insert_data)

    update_columns = [
        c.name for c in table.c if c not in list(table.primary_key.columns)
    ]

    on_conflict_statement = statement.on_conflict_do_update(
        constraint=constraint_name,
        set_={k: getattr(statement.excluded, k) for k in update_columns},
    )

    print(compile_query(on_conflict_statement))
    db_session.execute(on_conflict_statement)
    db_session.commit()


upsert(
    db_session=db_session,
    model=ContactType,
    insert_data=new_data,
    constraint_name=get_primary_key_constraint(table_name='contact_type'),
)


def table_and_column_name(table_name: str, schema: str):
    column_data = db_session.execute(
        f"""
        SELECT column_name 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE table_name = '{table_name}' 
        AND table_schema='{schema}'
        """
    )
    table_columns_list = []

    for col in column_data:
        table_columns_list.append(str(col[0]))
    return table_columns_list
