from rest_framework import serializers
from .models import Todo


class TodoSerializers(serializers.ModelSerializer):


    class Meta:
        model = Todo
        exclude = ['todo_title' , 'todo_description']   

