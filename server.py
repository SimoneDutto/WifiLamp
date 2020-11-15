from app import app

if __name__ == '__main__':
    run_with_ngrok(app) 
    app.run()