from app import create_app

from flask import jsonify, make_response
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")