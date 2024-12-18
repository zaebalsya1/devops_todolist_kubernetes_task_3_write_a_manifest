from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("liveness/", views.liveness, name="liveness"),
    path("readiness/", views.readiness, name="readiness"),
]
