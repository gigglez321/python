import uuid
# from db import items
from schemas import ItemSchema
from flask.views import MethodView
from flask_smorest import abort, Blueprint

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/items")
class ItemsList(MethodView):
    def get(self):
        return {"items": list(items.values())}


@blp.route("/item/<string:item_id>")
class ItemID(MethodView):
    def get(self,item_id):
        #funkcja request znajduje się w bibliotece Flask
        try:
            return items[item_id]
        except KeyError:
            return abort(404, message= "Item not found")

    @blp.arguments(ItemSchema)
    def put(self,item_data,item_id):
        # item_data = request.get_json()
        # if "price" not in item_data or "name" not in item_data:
        #     abort(400, message="Bad request. Ensute that name and price are in JSON payload")
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            return abort(404, message="Item not found")

    def delete(self,item_id):
        # funkcja request znajduje się w bibliotece Flask
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            return abort(404, message="Item not found")

@blp.route("/item")
class Item(MethodView):
    @blp.arguments(ItemSchema)
    def post(self,  item_data):
        # here not only we need to validate data exists,
        # But also what type of dara it is, Price should be float
        # item_data = request.get_json() # mozna usunąć ponieważ item_data spawdzane jest za pomocą Marshmallow

        # To zastępujemy przy użyciu Marshmallow
        # if (
        #         "store_id" not in item_data
        #         or "price" not in item_data
        #         or "name" not in item_data
        # ):
        #     return abort(
        #         404,
        #         message="Ensure that 'store_id', 'price' and 'name' are included in JSON payload"
        #     )

        for item in items.values():
            if (
                    item_data["name"] == item["name"]
                    and item_data["store_id"] == item["store_id"]
            ):
                return abort(
                    404,
                    message="Item already exist in store"
                )

        item_id = uuid.uuid4().hex
        item = {**item_data, "item_id": item_id}
        items[item_id] = item
        return item, 201
        # return 404 - not found