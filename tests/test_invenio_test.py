# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 CERN.
#
# Invenio-Test is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from invenio_test import InvenioTest


def test_version():
    """Test version import."""
    from invenio_test import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioTest(app)
    assert 'invenio-test' in app.extensions

    app = Flask('testapp')
    ext = InvenioTest()
    assert 'invenio-test' not in app.extensions
    ext.init_app(app)
    assert 'invenio-test' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to Invenio-Test' in str(res.data)
