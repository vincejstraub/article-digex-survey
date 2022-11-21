#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The utilities.py module includes methods used in two 
or more of the modules in the digex code package.
"""

from pathlib import Path


def get_parent_path():
    return Path(Path.cwd().parent)
              
                
def get_grandparent_path():
    return Path(Path.cwd().parent.parent)