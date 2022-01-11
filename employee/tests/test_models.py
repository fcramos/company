from django.test import TestCase
from ..models import Employee


class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(
            name='Jonh Do',
            email='jonh@company.com',
            department='Administration'
        )

    def test_created(self):
        "Should create a instance"
        Employee.objects.create(
            name='Fred',
            email='fred@company.com',
            department='Development'
        )
        self.assertEqual(Employee.objects.count(), 2)

    def test_update(self):
        "Should change a instance"
        instance = Employee.objects.first()
        instance.status = 1
        instance.save()
        self.assertEqual(instance.status, 1)

    def test_delete(self):
        "Should delete a instance"
        before = Employee.objects.count()
        instance = Employee.objects.first()
        instance.delete()
        after = Employee.objects.count()
        self.assertNotEqual(before, after)
