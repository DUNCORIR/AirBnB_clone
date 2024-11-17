#!/usr/bin/python3
"""
Initialize the models package.
"""


from models.engine.file_storage import FileStorage

# Create a unique instance of FileStorage
storage = FileStorage()

# Call reload() to populate storage with
# previously saved objects from file
storage.reload()
