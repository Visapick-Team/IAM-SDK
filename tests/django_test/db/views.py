from rest_framework.viewsets import ModelViewSet
from .models import SampleModel, SampleModelSerializer
from iam.permissions import AutoScopePermission, scope_permission
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['DELETE'])
@scope_permission(":profile:delete")
def SampleFunctionAPIView(request):
    return Response({"message": "Herkese selam"})


class SampleScopePermission(AutoScopePermission):
    _service_name = ""


class SampleModelView(ModelViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer
    permission_classes = [SampleScopePermission]

    object_name = "profile"

    def get_object(self):
        return self.get_queryset()[0]

    def get_queryset(self):
        return [SampleModel(id=1, name="test")]
