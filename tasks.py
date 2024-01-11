from __future__ import absolute_import
from celery import Celery
app = Celery('tasks',broker='pyamqp://guest@localhost//',backend='rpc://')

import mysql.connector

# db = mysql.connector.connect(user='root', password='qwerty123', host='127.0.0.1', database='restaurant_db')


@app.task
def update_status_accepted_to_preparing(document_id):
    print("update_status_accepted_to_preparing")
    db = mysql.connector.connect(user='root', password='qwerty123', host='127.0.0.1', database='restaurant_db')
    update_query = "UPDATE apis_pizzaordermodel SET order_status = 'Preparing' WHERE id = %s;"
    cursorA = db.cursor(buffered=True)
    cursorA.execute(update_query, (document_id,))
    db.commit()
    db.close()
    return

@app.task
def update_status_preparing_to_dispatched(document_id):
    print("update_status_preparing_to_dispatched")
    db = mysql.connector.connect(user='root', password='qwerty123', host='127.0.0.1', database='restaurant_db')
    update_query = "UPDATE apis_pizzaordermodel SET order_status = 'Dispacted' WHERE id = %s;"
    cursorA = db.cursor(buffered=True)
    cursorA.execute(update_query, (document_id,))
    db.commit()
    db.close()
    return

@app.task
def update_status_dispatched_to_delivered(document_id):
    print("update_status_dispatched_to_delivered")
    db = mysql.connector.connect(user='root', password='qwerty123', host='127.0.0.1', database='restaurant_db')
    update_query = "UPDATE apis_pizzaordermodel SET order_status = 'Delivered' WHERE id = %s;"
    cursorA = db.cursor(buffered=True)
    cursorA.execute(update_query, (document_id,))
    db.commit()
    db.close()
    return