from flaskblog import create_app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yctcfllhxlheos:8d68c07a4f5eb23a6439678b3d8dfaa477c66f58e7c6f2998e0880520a639b0e@ec2-54-163-140-104.compute-1.amazonaws.com:5432/deaehc7vkquo3l'
db=SQLAlchemy(app)
if __name__ == '__main__':
    app.run(debug=True)
