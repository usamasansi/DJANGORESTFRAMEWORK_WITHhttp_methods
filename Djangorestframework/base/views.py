from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializers
from .models import Todo

@api_view(['GET', 'POST', 'PATCH', 'DELETE', 'HEAD', 'PUSH', "ALL"])
def base(request):
    if request.method == 'GET':
        return Response({
        'status' : 200,
        'message' : 'yes django is working properly',
        'mathod_called' : "you called Get method"
    })

    elif request.method == 'POST':
        return Response({
        'status' : 300,
        'message' : 'yes django is working properly',
        'mathod_called' : "you called POST method"
    })
    elif request.method == 'ALL':
        return Response({
        'status' : 300,
        'message' : 'yes django is working properly',
        'mathod_called' : "you called ALL method"
    })
    elif request.method == 'HEAD':
        return Response({
        'status' : 300,
        'message' : 'yes django is working properly',
        'mathod_called' : "you called HEAD method"
    })
    elif request.method == 'DELETE':
        return Response({
        'status' : 300,
        'message' : 'yes django is working properly',
        'mathod_called' : "you called DELETE method"
    })
    elif request.method == 'PATCH':
        return Response({
        'status' : 350,
        'message' : 'yes django is working properly',
        'mathod_called' : "you called PATCH method"
    })
    else:
        return Response({
        'status' : 400,
        'message' : 'yes django is working properly',
        'mathod_called' : "you called invalid method"
    })


@api_view(['GET'])
def get_todo(request):
    todo_objc = Todo.objects.all()
    serializer = TodoSerializers(todo_objc , many = True)
    return Response({
        'status' : True,
        'message' : 'data ftched',
        'data' : serializer.data
    })



@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializers(data = data)
        if serializer.is_valid():
            
            serializer.save()      # save valid data to the data base
            return Response({
        'status' : True,
        'message' : 'success todo',
        'data' : serializer.data
        
    })  


        return Response({
        'status' : False,
        'message' : 'invalid todo',
        'data' : serializer.errors
        
    })    

    except Exception as e:
        print(e)
    return Response({
        'status' : False,
        'message' : 'something went wrong',
        
    })




    TodoSerializers