from app import crateApp

if __name__ == '__main__':
    app = crateApp()
    app.run(debug=True, use_reloader=True)
    