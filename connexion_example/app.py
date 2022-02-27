import connexion

host="localhost"
port=8000

app = connexion.FlaskApp(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)