from rest_framework import serializers

from .models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source="course.title", read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['image', 'address']


class CourseSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'





