# run.py

from app import create_app

app = create_app(config_name='development')  # ou 'production' para produção

if __name__ == '__main__':
    app.run(debug=True)

