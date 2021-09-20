from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .models import StudentsModel
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
from .validator import ApiValidations
import logging
from rest_framework.decorators import action, api_view

logger = logging.getLogger('django')


@api_view(['GET'])
def get_resultsapi(request):
    if request.method == 'GET':
        results = StudentsModel.objects.all()
        serializer = StudentSerializer(results, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def post_resultsapi(request):
    try:
        if request.method == 'POST':
            _dict = dict()
            _dict["data"] = request.data
            api_validation_object = ApiValidations(_dict["data"])
            if len(api_validation_object.validate_data()) > 0:
                logger.info("len of the validate data: {} , returning bad request .".format(api_validation_object.validate_data()))
                _dict["status"] = "400 Bad Request"
                _dict["message"] = api_validation_object.validate_data()
                return Response(_dict, status=status.HTTP_400_BAD_REQUEST)
            serializer = StudentSerializer(data=_dict["data"])
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_object(pk):
    try:
        results = StudentsModel.objects.get(pk=pk)
        return results
    except Exception:
        raise Http404


@api_view(['GET'])
def retrieve_resultsapi(request, pk):
    results = get_object(pk)
    if request.method == 'GET':
        serializer = StudentSerializer(results)
        return Response(serializer.data)


@api_view(['PUT'])
def put_resultsapi(request, pk):
    if request.method == 'PUT':
        _dict = dict()
        _dict["data"] = request.data
        api_validation_object = ApiValidations(_dict["data"])
        if len(api_validation_object.validate_data()) > 0:
            _dict["status"] = "400 Bad Request"
            _dict["message"] = api_validation_object.validate_data()
            return Response(_dict, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentSerializer(data=_dict["data"])
        if serializer.is_valid():
            logger.info("returning status 201")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_resultsapi(request, pk):
    if request.method == 'DELETE':
        results = get_object(pk)
        results.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
