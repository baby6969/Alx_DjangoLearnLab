from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import FollowSerializer, FollowerListSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        target_id = serializer.validated_data['target_user_id']
        if target_id == request.user.id:
            return Response({'detail': 'Cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(User, id=target_id)
        request.user.following.add(target)
        data = FollowerListSerializer(request.user.following.all(), many=True).data
        return Response({'following': data}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        target_id = serializer.validated_data['target_user_id']
        target = get_object_or_404(User, id=target_id)
        request.user.following.remove(target)
        data = FollowerListSerializer(request.user.following.all(), many=True).data
        return Response({'following': data}, status=status.HTTP_200_OK)

class FollowingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowerListSerializer

    def get_queryset(self):
        return self.request.user.following.all()

class FollowersListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowerListSerializer

    def get_queryset(self):
        return self.request.user.followers.all()
