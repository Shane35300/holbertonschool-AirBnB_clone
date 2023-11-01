from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
storage.classes = {'BaseModel': BaseModel}
 