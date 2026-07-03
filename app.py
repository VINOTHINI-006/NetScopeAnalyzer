from flask import Flask, render_template
from packet_sniffer import get_packets

app = Flask(__name__)

@app.route("/")
def home():
    packets = get_packets()
    return render_template("index.html", packets=packets)

if __name__ == "__main__":
    app.run(debug=True)