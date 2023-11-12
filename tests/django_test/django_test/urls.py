from db.views import SampleModelView, SampleFunctionAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = "db"
router = DefaultRouter()
router.register(r"model", SampleModelView, basename="model-viewset")

urlpatterns = router.get_urls()
urlpatterns.append(path("api_view/", SampleFunctionAPIView))
