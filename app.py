from flask import Flask, request, jsonify

app_name = "Python App With Flask, HTML, And REST"
app = Flask(app_name)
client = "VMware"
framework = "Python with Pipenv"

messages = [
    {
        'client': client,
        'framework': framework,
        'msg_subject': 'Secure Software Supply Chains Are Great!',
        'msg_body': 'With A Secure Software Supply Chain, Deploying Python Code To PROD is Safe, Reliable, And Fast!'
    }
]

@app.route("/")
def hello():
    return f"""
    <html>
      <head><title>Simple Hello Page</title></head>
      <body>
        <h1>Hello from {client} using {framework}!</h1>
      </body>
    </html>
    """

@app.route('/messages')
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
