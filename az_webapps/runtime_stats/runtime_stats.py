from flask import Flask
app = Flask(__name__)

@app.route("/runtime_stats")
def runtime_stats():
    f = open("/proc/self/cgroup", "r")
    return f.read()