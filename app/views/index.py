import re
import json

from flask import render_template, request, abort
from  sqlalchemy.sql.expression import func, select

from app import app, db
from app.models import Person


@app.route('/')
def index():
    names =  Person.query.all()
    return render_template('index.html', names=names)


@app.route('/add/', methods=["POST"])
def add_name():
    name = json.loads(request.data).get('name') or None
    try:
        p = Person(name=name)
        db.session.add(p)
        db.session.commit()
    except ValueError:
        abort(400, json.dumps({"status": "success"}))
    return json.dumps({"name": {'name' : p.name, 'id' : p.id}})

@app.route('/delete/', methods=["POST"])
def delete_name():
    id = int(json.loads(request.data).get('id')) or None
    p = Person.query.filter_by(id=id).first_or_404()
    db.session.delete(p)
    db.session.commit()
    return json.dumps({"status": "success"})



@app.route('/winners/')
def rand():
    rand_names = Person.query.order_by(func.random()).limit(3).all()
    response_dict = {
        'names' : [{'name' : p.name, 'id' : p.id} for p in rand_names]
    }
    return json.dumps(response_dict)

@app.route('/names/')
def names():
    names = Person.query.all()
    response_dict = {
        'names' : [{'name' : p.name, 'id' : p.id} for p in names]
    }
    return json.dumps(response_dict)

