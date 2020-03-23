#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of forecast.
# https://github.com/kaija/forecast.git

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2020, Kaija <kaija.chang@gmail.com>

from preggy import expect

from forecast import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
