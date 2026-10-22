from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from . import permissions
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['full_name', 'phone_number', 'address']
    ordering_fields = ['id', 'full_name', 'birth_year', 'course']
    filterset_fields = {
        'course__title': ['exact'],
        'birth_year': ['exact', 'lt', 'lte', 'gt', 'gte'],
    }

