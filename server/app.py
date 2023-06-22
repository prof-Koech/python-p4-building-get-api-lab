#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@@app.route("/bakeries", methods=["GET"])
def get_bakeries():
    bakeries = Bakery.query.all()
    bakery_list = []
    for bakery in bakeries:
        bakery_data = {
            "id": bakery.id,
            "name": bakery.name,
            # Include other bakery attributes as needed
        }
        bakery_list.append(bakery_data)
    return jsonify(bakery_list)


from flask import Flask, jsonify, make_response
from models import Bakery, BakedGood


@app.route("/bakeries/<int:id>", methods=["GET"])
def get_bakery(id):
    bakery = Bakery.query.get(id)

    if bakery is None:
        response = {"error": "Bakery not found"}
        return jsonify(response), 404

    baked_goods = [baked_good.name for baked_good in bakery.baked_goods]

    bakery_data = {
        "id": bakery.id,
        "name": bakery.name,
        "baked_goods": baked_goods
        # Include other bakery attributes as needed
    }

    return jsonify(bakery_data)


@app.route("/baked_goods/by_price", methods=["GET"])
def get_baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()

    baked_goods_data = []
    for baked_good in baked_goods:
        baked_good_data = {
            "id": baked_good.id,
            "name": baked_good.name,
            "price": baked_good.price,
            # Include other baked good attributes as needed
        }
        baked_goods_data.append(baked_good_data)

    return jsonify(baked_goods_data)


@app.route("/baked_goods/most_expensive", methods=["GET"])
def get_most_expensive_baked_good():
    most_expensive_baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()

    if most_expensive_baked_good is None:
        # Handle the case when no baked goods are available
        return jsonify({"message": "No baked goods found."}), 404

    baked_good_data = {
        "id": most_expensive_baked_good.id,
        "name": most_expensive_baked_good.name,
        "price": most_expensive_baked_good.price,
        # Include other baked good attributes as needed
    }

    return jsonify(baked_good_data)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
