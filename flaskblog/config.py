import os
import psycopg2


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = psycopg2.connect('postgres://yctcfllhxlheos:8d68c07a4f5eb23a6439678b3d8dfaa477c66f58e7c6f2998e0880520a639b0e@ec2-54-163-140-104.compute-1.amazonaws.com:5432/deaehc7vkquo3l', sslmode='require')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'charan.potnuru3@gmail.com'
    MAIL_PASSWORD = 'bhaskar170111'