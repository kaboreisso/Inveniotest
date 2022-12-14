# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 CERN.
#
# Invenio-Test is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module that adds more fun to the platform."""

from .ext import InvenioTest
from .version import __version__

__all__ = ('__version__', 'InvenioTest')
