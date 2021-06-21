#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Provides NumberList and FrequencyDistribution, classes for statistics.
NumberList holds a sequence of numbers, and defines several statistical
operations (mean, stdev, etc.) FrequencyDistribution holds a mapping from
items (not necessarily numbers) to counts, and defines operations such as
Shannon entropy and frequency normalization.
"""

import os    # standard library
import sys

import requests  # 3rd party packages

from mypackage import (  # local source
    mymodule,
    myothermodule,
)

__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"


class NumberList(list):
    pass    #much code deleted
class FrequencyDistribution(dict):
    pass    #much code deleted
  
  
if __name__ == '__main__':   
    pass 
