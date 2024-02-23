import uuid
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True , editable=False , default=uuid.uuid4())
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add= True)

    class Meta:
        abstract = True



class Todo(BaseModel): 
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)




class Item(models.Model):
    name =models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)