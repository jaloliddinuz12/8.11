import json

from rest_framework.test import APITestCase
from django.urls import reverse


from .models import Student, Course
from .serializers import StudentSerializer
from django.contrib.auth.models import User
class StudentTestCase(APITestCase):


    def setUp(self):


        self.user1 = User.objects.create_user(username="Toxir", password='Aa123456@')


        login_url = reverse('token_obtain_pair')
        response = self.client.post(login_url, data={"username":  "Toxir", "password": "Aa123456@"})
        self.assertEqual(response.status_code, 200)
        access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)


        self.course1 = Course.objects.create(title="Python", durations=9)
        self.course2 = Course.objects.create(title="Web", durations=10)

        self.student1 = Student.objects.create(full_name="Toxir", address="andijon", course=self.course1)
        self.student2 = Student.objects.create(full_name='Sobir', address="tosh", course=self.course2)
        self.student3 = Student.objects.create(full_name="Bakir", address="Fergana", course=self.course1)


    def test_get(self):
        url = reverse('talaba-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        serializer = StudentSerializer([self.student1, self.student2, self.student3], many=True)
        self.assertEqual(response.data, serializer.data)


    def test_get_search(self):
        url = reverse('talaba-list')

        self.client.force_login(self.user1)
        response = self.client.get(url, data={'search': 'Fergana'})



        self.assertEqual(response.status_code, 200)
        serializer = StudentSerializer([self.student1, self.student3], many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_ordering(self):
        url = reverse('talaba-list')

        self.client.force_login(self.user1)
        response = self.client.get(url, data={'ordering': 'full_name'})



        self.assertEqual(response.status_code, 200)
        serializer = StudentSerializer([self.student3, self.student2, self.student1], many=True)
        self.assertEqual(response.data, serializer.data)


    # def test_filter_backend(self):
    #     url = reverse('talaba-list')
    #
    #     self.client.force_login(self.user1)
    #
    #     response = self.client.get(url, data={'course__title': self.course1.title})
    #
    #     self.assertEqual(response.status_code, 200)
    #     serializer = StudentSerializer(expected_students, many=True)
    #     self.assertEqual(response.data, serializer.data)


    def test_create(self):
        url = reverse('talaba-list')
        data = {
            "full_name": "Toxir Sobirov",
            'phone_number': "+9989",
            'course': 2
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user1)
        response = self.client.post(url, data=json_data, content_type="application/json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Student.objects.all().count(), 4)

    def test_update(self):
        url = reverse('talaba-detail', args=(self.student1.pk,))
        data = {
            "full_name": self.student1.full_name,
            'phone_number': self.student1.phone_number,
            'address': "andijon",
            'course': self.student1.course.pk
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user1)
        response = self.client.put(url, data=json_data, content_type="application/json")

        self.assertEqual(response.status_code, 200)

        self.student1.refresh_from_db()
        self.assertEqual(response.data.get('address'), self.student1.address)

    def test_delete(self):
        url = reverse('talaba-detail', args=(self.student1.pk,))

        self.client.force_login(self.user1)

        respone = self.client.delete(url)

        self.assertEqual(respone.status_code, 204)
        self.assertEqual(Student.objects.all().count(), 2)

    def test_partial_update(self):
        url = reverse('talaba-detail', args=(self.student1.pk,))
        data = {
            'address': "andijon",
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user1)
        response = self.client.patch(url, data=json_data, content_type="application/json") 