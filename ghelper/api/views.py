from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Frame
from .serializers import FrameSerializer
from .gesture import gesture


class FrameViewSet(viewsets.ViewSet):

    def create(self, request):
        data = {
            'image': request.data.get('image', None),
            'result': 'Default'
        }
        serializer = FrameSerializer(data=data)
        if serializer.is_valid():
            frame = serializer.save()  # This will call the save method of Frame model
            return Response(frame.result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
