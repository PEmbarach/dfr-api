from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serialiazers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permission.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class FollowerDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = [IsOwnerOrReadOnly]
        serializer_class = FollowerSerializer
        queryset = Follower.objects.all()
