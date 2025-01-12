def insert_val(cursor, datafile):
    CREATE_TABLE_QUERY= """
    CREATE TABLE IF NOT EXISTS sample_table (
    id SERIAL PRIMARY KEY,
    NAME VARCHAR(50),
    DEPARTMENT VARCHAR(50)
    )"""

    cursor.execute(CREATE_TABLE_QUERY)

    name= datafile.get("name")
    department= datafile.get("department")

    INSERT_QUERY= """
    INSERT INTO sample_table (NAME, DEPARTMENT) VALUES (%s, %s)
    """
    
    cursor.execute(INSERT_QUERY, (name, department))

def show_all_data(cursor):
    SHOW_QUERY= """SELECT * FROM sample_table"""

    cursor.execute(SHOW_QUERY)
    rows= cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]

    # Format the result as a list of dictionaries
    result = [dict(zip(column_names, row)) for row in rows]

    return result
