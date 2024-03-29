#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of apache_spark.
# https://github.com/josl/ApacheSpark_02817

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros & Kosai Al-Nakeeb <bellod.cisneros@gmail.com & kosai@cbs.dtu.dk>

from preggy import expect

from apache_spark import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
