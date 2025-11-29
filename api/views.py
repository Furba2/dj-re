from rest_framework import generics, permissions
from .serializers import TopicSerializer
from logs.models import Topic

class TopicListCreate(generics.ListCreateAPIView):

    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Topic.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TopicRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Topic.objects.filter(user=user)