import duckdb


con = duckdb.connect()

# Create the students table and add its data.
con.sql("""
CREATE TABLE students AS
SELECT * FROM (VALUES
    ('Guide', 72),
    ('Poom', 88),
    ('Indy', 91),
    ('Audy', 67),
    ('M', 84),
    ('Acare', 76),
    ('Sun', 79),
    ('Ryu', 93)
) AS data(name, score)
""")


con.sql("SELECT * FROM students").show()

con.sql("SELECT name, score FROM students").show()

con.close()