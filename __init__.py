from models.engine.file_storage import FileStorage

# Create a storage instance
storage = FileStorage()

# Load data from the JSON file into the storage instance
storage.reload()
