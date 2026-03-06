from flask import Flask,jsonify
app = Flask(__name__)

def extract_info():
    counts = {"Info":0,"Warning":0,"Error":0}
    
    with open("Log.txt","r") as file:
        for line in file:
            if "INFO" in line:
                counts["Info"] += 1
            elif "WARNING" in line:
                counts["Warning"] += 1
            elif "ERROR" in line:
                counts["Error"] += 1
    return counts
@app.route("/logs")
def logs():
    return jsonify(extract_info())
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
        