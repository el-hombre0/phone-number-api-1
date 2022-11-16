from fastapi import FastAPI, Request
import uvicorn
import mysql.connector
 
app = FastAPI()
 
 
@app.post("/api/contacts/add/{phone}/{address}")
async def add(phone: str, address: str) -> dict[str, str]:
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="phoneDB",
    )
 
    cursor = db.cursor()
    sql = "insert into contacts (phone, address) values (%s, %s)"
    val = (phone, address)
 
    try:
        cursor.execute(sql, val)
        db.commit()
 
        cursor.close()
        db.close()
        return {"status": "OK"}
    except Exception as e:
        return {"status": "FAIL", "reason": str(e)}
 
 
@app.get("/api/contacts/")
async def get_all() -> list:
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="phoneDB",
    )
 
    cursor = db.cursor()
    sql = "select * from contacts"
    cursor.execute(sql)
    result = []
    for item in cursor.fetchall():
        result.append({"id": item[0], "phone": item[1], "address": item[2]})
 
    cursor.close()
    db.close()
    return {"status": "OK", "result": result}
 
 
@app.get("/api/contacts/{id}")
async def get_by_id(id: int) -> dict[str, str]:
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="phoneDB",
    )
 
    cursor = db.cursor()
    sql = "select * from contacts where id = {}".format(id)
    cursor.execute(sql)
    item = cursor.fetchone()
    if item == None:
        return {"status": "OK", "result": ""}
 
    result = {"id": item[0], "phone": item[1], "address": item[2]}
 
    cursor.close()
    db.close()
    return {"status": "OK", "result": result}
 
 
@app.put("/api/contacts/update/{id}/{key}/{value}")
async def update(id: int, key: str, value: str) -> dict[str, str]:
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="phoneDB",
    )
 
    cursor = db.cursor()
    sql = f"update contacts set `{key}` = '{value}' where id = '{id}'"
    print(sql)
 
    try:
        cursor.execute(sql)
        db.commit()
 
        cursor.close()
        db.close()
        return {"status": "OK"}
    except Exception as e:
        return {"status": "FAIL", "reason": str(e)}
 
 
@app.delete("/api/contacts/delete/{id}")
async def delete(id: int) -> dict[str, str]:
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="phoneDB",
    )
 
    cursor = db.cursor()
    sql = f"delete from contacts where id = '{id}'"
 
    try:
        cursor.execute(sql)
        db.commit()
 
        cursor.close()
        db.close()
        return {"status": "OK"}
    except Exception as e:
        return {"status": "FAIL", "reason": str(e)}
 
 
@app.get("/")
async def index() -> dict[str, str]:
    return {"status": "OK"}
 
 
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
 