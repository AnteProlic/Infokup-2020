def dev_config(flask_app):
    config = flask_app.config
    config [
        'SECRET_KEY'
    ] = '9A5143FA274EFCAB9DD2D18E52BFC'
    config['DEBUG'] = True
    config[
        'MONGO_URI'
    ] = 'mongodb://127.0.0.1:27017/testdb'
    return config
