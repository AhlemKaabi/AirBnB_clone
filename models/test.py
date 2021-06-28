from engine.file_storage import FileStorage
from base_model import BaseModel

my_model = BaseModel()
my_model.name = "ala"
my_model.number = 5
print(my_model)

FileStorage.new(my_model)
FileStorage.save(my_model)
