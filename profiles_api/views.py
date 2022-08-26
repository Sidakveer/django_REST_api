from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test api view"""

    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        "Uses HTTP methods as function (get, post, put, patch, delete)",
        "Is similar to a traditional django view",
        "Gives us most control over our application logic",
        "is mapped manually to urls"

        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """create a hello message with  our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})

        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """make a partial update on an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({"method": "DELETE"})



class HelloViewSet(viewsets.ViewSet):
    """test api view set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            "use actions (list, create, retrieve, partial_update)",
            "automatically maps to urls using routers",
            "provides more functionality with less code",
        ]

        return Response({"message": "hello", "a_viewset": a_viewset})

    def create(self, request):
        """create a hello msg"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"hello {name}"
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({"http method": "GET"})

    def update(self, request, pk=None):
        """handle updating an object"""
        return Response({"http method": "PUT"})

    def partial_update(self, request, pk=None):
        """parially update an object"""
        return Response({"http method": "PATCH"})

    def destroy(self, request, pk=None):
        """Removing an object from the database"""
        return Response({"http method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
