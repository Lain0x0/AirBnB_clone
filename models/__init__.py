#!/usr/bin/python3
"""_init_ imports modules and packages """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()