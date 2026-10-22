from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import (StudentViewSet, CourseViewSet)

router = DefaultRouter()

router.register('students', StudentViewSet, basename='talaba')
router.register('courses', CourseViewSet)

urlpatterns = router.urls

r





# urlpatterns = [
#     path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
#     # path('students/course/<int:course_id>/', StudentListAPIView.as_view()),
#     path('students/<int:pk>/', StudentViewSet.as_view(
#         {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
#     )),
# ]