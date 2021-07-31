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


# logging.basicConfig(filename='C:/Users/abina/Desktop/MyFiles/projects/MetricResults/server.log', encoding='utf-8',
#                     level=logging.INFO,
#                     format='%(asctime)s, %(levelname)s, %(filename)s, %(funcName)s(%(lineno)d), %(message)s')
# logging.debug("Test logging")
# logging.info("Test Logging")
# logging.error("test logging")

# class ResultsApi(APIView):
#     def get(self, request):
#         result = StudentsModel.objects.all()
#         serializer = StudentSerializer(result, many=True)
#         return Response(serializer.data)
#
#     @action(method=['post'], detail=True, url_path='post-data', url_name='post_data')
#     def post(self, request):
#         data = request.data
#         try:
#             api_validation_object = ApiValidations()
#             if len(api_validation_object.validate_data(data)) > 0:
#                 return Response(api_validation_object.validate_data(data), status=status.HTTP_400_BAD_REQUEST)
#         except:
#             logger.exception("Error Happened.")
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class GetResultsApi(APIView):
#     def get_object(self, pk):
#         try:
#             return StudentsModel.objects.get(pk=pk)
#         except Exception:
#             raise Http404
#
#     def get(self, request, pk):
#         result = self.get_object(pk)
#         serializer = StudentSerializer(result)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         result = self.get_object(pk)
#         data = request.data
#         logger.info(result, type(result))
#         logger.info(data, type(data))
#         api_validation_object = ApiValidations()
#         if len(api_validation_object.validate_data(data)) > 0:
#             return Response(api_validation_object.validate_data(data), status=status.HTTP_400_BAD_REQUEST)
#         serializer = StudentSerializer(result, data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         result = self.get_object(pk)
#         result.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def patch(self, request, pk):
#         result = self.get_object(pk)
#         data = request.data
#         api_validation_object = ApiValidations()
#         if len(api_validation_object.validate_data(data)) > 0:
#             return Response(api_validation_object.validate_data(data), status=status.HTTP_400_BAD_REQUEST)
#         serializer = StudentSerializer(result, data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            data = request.data
            api_validation_object = ApiValidations(data)
            if len(api_validation_object.validate_data()) > 0:
                logger.info("len of the validate data: {} , returning bad request .".format(api_validation_object.validate_data()))
                return Response(api_validation_object.validate_data(), status=status.HTTP_400_BAD_REQUEST)
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                logger.info("returning status 201")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.info("returning bad request .")
            return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)
    except:
        logger.exception("exception happened,  returning 500")
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
        results = get_object(pk)
        data = request.data
        api_validation_object = ApiValidations(data)
        if len(api_validation_object.validate_data()) > 0:
            return Response(api_validation_object.validate_data(), status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentSerializer(results, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_resultsapi(request, pk):
    if request.method == 'DELETE':
        results = get_object(pk)
        results.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
