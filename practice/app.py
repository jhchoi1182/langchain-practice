from flask import Flask, request, jsonify

from ice_break import ice_break_with

app = Flask(__name__)


@app.route("/linkedin_uer_summary", methods=["POST"])
def linkedin_uer_summary():
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with(name=name)
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url
        }
    )


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)