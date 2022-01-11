from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from employee.models import Employee


class EmployeeTest(APITestCase):
    url = reverse('employee-list')
    data = {
        'name': 'Jonh Do',
        'email': 'jonh@company.com',
        'department': 'Administration'
    }

    def test_create_employee(self):
        """
        Ensure we can create a new employee object.
        """
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)

    def test_change_status(self):
        """
        Should change employee status by endpoint
        """
        response = self.client.post(self.url, self.data, format='json')
        pk = response.data['id']
        url = reverse('employee-detail', kwargs={'pk': pk})

        data = self.client.get(url).data
        data.update({'department': 'Development'})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['department'], 'Development')

    def test_delete_employee(self):
        """
        Should delete a employee object
        """
        response = self.client.post(self.url, self.data, format='json')
        pk = response.data['id']
        url = reverse('employee-detail', kwargs={'pk': pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(self.client.get(self.url).data), 0)
