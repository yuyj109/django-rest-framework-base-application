from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers


class Profile(APIView):

    def get(self, request, format=None):

        user = request.user

        if user.is_anonymous:
            return Response(status=status.HTTP_204_NO_CONTENT)

        user_profile = models.Profile.objects.filter(user=user).get()

        serializer = serializers.ProfileSerializer(user_profile)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
