from flask import Flask, jsonify
import pytest


def create_app(env=None):
    app = Flask(__name__)
    return app


@pytest.fixture
def app():
    return create_app("test_marshmallow_3")


@pytest.fixture
def client(app):
    return app.test_client()
