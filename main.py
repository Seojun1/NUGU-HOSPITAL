from api import NuguApi

app = NuguApi()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
