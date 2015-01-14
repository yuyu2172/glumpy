# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
"""
Transverse Mercator projection
http://en.wikipedia.org/wiki/Transverse_Mercator_projection
"""
from glumpy import library
from . transform import Transform


class TransverseMercatorProjection(Transform):
    """ Transverse Mercator projection """

    aliases = {  }

    def __init__(self, *args, **kwargs):
        """
        Initialize the transform.
        Note that parameters must be passed by name (param=value).

        Kwargs parameters
        -----------------
        """

        code = library.get("transforms/transverse_mercator.glsl")
        Transform.__init__(self, code, *args, **kwargs)


    def __getitem__(self, key):
        """ Override getitem to enforce aliases """

        key = self.__class__.aliases.get(key, key)
        return Transform.__getitem__(self, key)


    def __setitem__(self, key, value):
        """ Override getitem to enforce aliases """

        key = self.__class__.aliases.get(key, key)
        Transform.__setitem__(self, key, value)


    def on_attach(self, program):
        """ Initialization event """

        pass