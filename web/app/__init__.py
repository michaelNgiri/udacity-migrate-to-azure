import redis
import os
import logging
from app.cache import CacheFacade
from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from azure.servicebus import QueueClient

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

app.secret_key = app.config.get('SECRET_KEY')

queue_client = QueueClient.from_connection_string(app.config.get('SERVICE_BUS_CONNECTION_STRING'),
                                                  app.config.get('SERVICE_BUS_QUEUE_NAME'))

db = SQLAlchemy(app)

cache = CacheFacade(session, redis.StrictRedis(
    host=app.config.get('REDIS_HOST'),
    port=6380,
    password=app.config.get('REDIS_PKEY'),
    ssl=True)
)
logging.info('Cache {} is connected? {}'.format(cache.name(), cache.isConnected()))
print('Cache {} is connected? {}'.format(cache.name(), cache.isConnected()))

from . import routes