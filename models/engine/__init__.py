#!/usr/bin/python3
"""Init file for engine module."""
from .file_storage import FileStorage

storage = FileStorage()
storage.reload()
