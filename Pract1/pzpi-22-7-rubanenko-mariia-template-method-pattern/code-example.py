from flask import Flask, request, jsonify

app = Flask(__name__)

# Base class implementing the Template Method for handling API requests
class BaseAPIHandler:
    def handle_request(self):
        """Template Method: defines the general algorithm for handling API requests"""
        if request.method == "GET":
            data = self.get_data()
        elif request.method == "POST":
            data = self.create_data()
        else:
            return jsonify({"error": "Method not supported"}), 405

        return self.format_response(data)

    def format_response(self, data):
        """Formats the response into a consistent JSON structure"""
        return jsonify({"status": "success", "data": data})

    def get_data(self):
        """Abstract method for retrieving data (must be implemented in subclass)"""
        raise NotImplementedError("The get_data() method must be implemented in a subclass")

    def create_data(self):
        """Abstract method for creating data (must be implemented in subclass)"""
        raise NotImplementedError("The create_data() method must be implemented in a subclass")


# API implementation for handling orders
class OrderAPI(BaseAPIHandler):
    def get_data(self):
        """Retrieve a list of orders"""
        return [{"order_id": 1, "amount": 100}, {"order_id": 2, "amount": 200}]

    def create_data(self):
        """Create a new order"""
        new_order = request.json
        return {"message": "Order created", "order": new_order}


# API implementation for handling payments
class PaymentAPI(BaseAPIHandler):
    def get_data(self):
        """Retrieve a list of payments"""
        return [{"payment_id": 101, "status": "Completed"}, {"payment_id": 102, "status": "Pending"}]

    def create_data(self):
        """Process a new payment"""
        new_payment = request.json
        return {"message": "Payment processed", "payment": new_payment}


# Register routes in Flask
@app.route("/orders", methods=["GET", "POST"])
def orders():
    return OrderAPI().handle_request()

@app.route("/payments", methods=["GET", "POST"])
def payments():
    return PaymentAPI().handle_request()

if __name__ == "__main__":
    app.run(debug=True)
