from django.core.files.storage import default_storage
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ExtractedText
from .serializers import ExtractedTextSerializer
from .utils import extract_text_from_pdf, extract_text_from_image

from rest_framework.generics import ListAPIView
from .models import ExtractedText
from .serializers import ExtractedTextSerializer
from django.utils.datastructures import MultiValueDictKeyError

# API View to retrieve all extracted text
class ExtractedTextListView(ListAPIView):
    queryset = ExtractedText.objects.all()
    serializer_class = ExtractedTextSerializer

class FileUploadView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            if 'file' not in request.FILES:
                return Response({'error': 'No file was uploaded. Make sure to send a file with key "file".'}, status=status.HTTP_400_BAD_REQUEST)

            file_obj = request.FILES['file']
            file_path = default_storage.save(file_obj.name, file_obj)
            full_path = default_storage.path(file_path)

            # Determine file type and extract text
            if file_obj.name.endswith('.pdf'):
                extracted_text = extract_text_from_pdf(full_path)
                file_type = 'PDF'
            elif file_obj.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                extracted_text = extract_text_from_image(full_path)
                file_type = 'Image'
            else:
                return Response({'error': 'Unsupported file type'}, status=status.HTTP_400_BAD_REQUEST)

            # Store extracted text in the database
            extracted_entry = ExtractedText.objects.create(content=extracted_text, file_type=file_type)
            return Response(ExtractedTextSerializer(extracted_entry).data, status=status.HTTP_201_CREATED)

        except MultiValueDictKeyError:
            return Response({'error': 'File not provided in the request'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
