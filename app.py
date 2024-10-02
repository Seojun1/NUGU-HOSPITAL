from api import NuguApi

if __name__ == "__main__":
    app = NuguApi()

    app.run(host="0.0.0.0", port=5001, debug=True)
