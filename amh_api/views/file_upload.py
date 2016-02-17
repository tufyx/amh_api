from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from uuid import uuid4
from amh_api.serializers import AssetSerializer
from rest_framework.generics import RetrieveAPIView


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser)

    def post(self, request, format=None):
        file_obj = request.data['file']
        file_id = '{file_id}.png'.format(file_id=uuid4())
        filename = '/Users/tufyx/Workspace/web/amh/api/amh_api/static/images/{file_id}'.format(file_id=file_id)
        with open(filename, 'wb+') as filename:
            for chunk in file_obj.chunks():
                filename.write(chunk)
        serializer = AssetSerializer({'file_name': file_id})
        return Response(serializer.data)
