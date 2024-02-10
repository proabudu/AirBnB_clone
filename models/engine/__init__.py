#!/usr/bin/python3
"""Init file for engine module."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
