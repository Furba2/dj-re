from rest_framework import generics, permissions
from .s import TS
from ls.models import T

class TListCreate(generics.ListCreateAPIView):

    serializer_class = TS
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return T.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TS
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return T.objects.filter(user=user)