from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import io


@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)

        if id is not None:
            try:
                stu = Student.objects.get(id=id)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Student created successfully'}, status=201)
        return JsonResponse(serializer.errors, status=400)
    

    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Student updated successfully'})
        return JsonResponse(serializer.errors, status=400)
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        stu.delete()
        return JsonResponse({'message': 'Student deleted successfully'}, status=204)
    

# @csrf_exempt
# def student_api(request,id=None):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)

#         if id is not None:
#             try:
#                 stu = Student.objects.get(id=id)
#             except Student.DoesNotExist:
#                 return JsonResponse({'error': 'Student not found'}, status=404)
#             serializer = StudentSerializer(stu)
#             return JsonResponse(serializer.data)
#         else:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu, many=True)
#             return JsonResponse(serializer.data, safe=False)

#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message': 'Student created successfully'}, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         try:
#             stu = Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return JsonResponse({'error': 'Student not found'}, status=404)
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message': 'Student updated successfully'})
#         return JsonResponse(serializer.errors, status=400)

#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         try:
#             stu = Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return JsonResponse({'error': 'Student not found'}, status=404)
#         stu.delete()
#         return JsonResponse({'message': 'Student deleted successfully'}, status=204)
