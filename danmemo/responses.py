from flask import jsonify

def response(status, data, message, code):
    return {
        'sucess': status,
        'data': data,
        'messages': message,
        'code': code,
    }

def bad_request():
    return jsonify(
        response(
            False,
            {},
            'Bad request',
            400
        )
    ), 400

def not_found():
    return jsonify(
        response(
            False,
            {},
            'Resource not found',
            404
        )
    ), 400

def resp(data):
    return jsonify(
        response(
            True,
            data,
            'Successful request',
            200
        )
    ), 200
