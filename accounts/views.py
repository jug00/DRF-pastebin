from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmailConfirmSerializer
from rest_framework.reverse import reverse_lazy
from rest_framework.status import HTTP_200_OK


class ConfirmEmailView(APIView):
    def get(self, request, key, format=None):
        serializer = EmailConfirmSerializer(instance={"key": key, "url": reverse_lazy("rest_verify_email", request=request)})
        return Response(serializer.data, status=HTTP_200_OK)





