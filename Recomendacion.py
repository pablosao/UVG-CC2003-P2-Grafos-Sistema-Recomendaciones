#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

"""
Created on Tue May 21 19:02:48 2019

@author: Pablo Sao
@author: Andrea Elias
@author: Juan Fernando de Leon
"""

import ControladorGrafo



ControladorGrafo.FindMatch('Cálido'.encode('raw_unicode_escape').decode('utf-8'),
                           'QQ'.encode('raw_unicode_escape').decode('utf-8'),
                           'Aventura'.encode('raw_unicode_escape').decode('utf-8')
                           ,'Amigos/as'.encode('raw_unicode_escape').decode('utf-8'))