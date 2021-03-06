import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = ('postgres://mjigjcdxhoacny:326f53fd1227b9048314cce344089aaccfbe74e516eef71efbee19d970a6257c@ec2-54-197-228-62.compute-1.amazonaws.com:5432/df43bb7tk1sdos')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'charan.potnuru3@gmail.com'
    MAIL_PASSWORD = 'bhaskar170111'