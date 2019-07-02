from flask import Flask, jsonify, request, make_response, url_for

import config
import dbapi


app = Flask(__name__)
db = dbapi.get_impl()


@app.route("/report", methods=["POST"])
def upload_report():
    if request.content_type != "application/json":
        return make_response("JSON data expected", 401, {})
    data = request.get_json()
    report_id = db.create_report(data)
    res = {"status": "ok", "id": report_id, "url": url_for("show_report", report_id=report_id)}
    return jsonify(res)


@app.route("/report/<report_id>")
def show_report(report_id):
    data = db.get_report(report_id)
    res = {"status": "ok", "content": data}
    return jsonify(res)


if __name__ == "__main__":
    app.run(host=config.WEBSERVER_HOST, port=config.WEBSERVER_PORT, debug=True)
