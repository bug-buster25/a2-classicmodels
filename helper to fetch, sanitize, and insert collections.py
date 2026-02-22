def migrate_table_to_collection(sql_query, mongo_collection, transform_func=None):
    mysql_cursor.execute(sql_query)
    rows = mysql_cursor.fetchall()
    if transform_func:
        rows = [transform_func(row) for row in rows]
    sanitized_rows = [sanitize_for_mongo(row) for row in rows]
    if sanitized_rows:
        mongo_collection.insert_many(sanitized_rows)
