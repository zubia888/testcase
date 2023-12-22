import sentry_sdk
from flask import Flask

sentry_sdk.init(
    dsn="https://444ea0895fcd82446c78575f505f78c3@o4506439037288448.ingest.sentry.io/4506439041548288",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    1/0  # raises an error
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
