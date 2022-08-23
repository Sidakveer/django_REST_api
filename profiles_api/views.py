from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        "Uses HTTP methods as function (get, post, put, patch, delete)",
        "Is similar to a traditional django view",
        "Gives us most control over our application logic",
        "is mapped manually to urls"

        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})
