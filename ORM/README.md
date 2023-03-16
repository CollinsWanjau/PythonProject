# 0x0F. Python - Object-relational mapping

### without an ORM
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root",
password="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### With an ORM
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}').format
    ("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create+all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL
query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close
