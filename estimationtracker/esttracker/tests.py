import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.test.client import Client
from django.urls import resolve, reverse

from .forms import CreateTask
from .models import *
from .utils import get_correctness, get_estimation_time, time_in_sec
from .views import *

# Create your tests here.

# It tests if a valid task can be created and if an invalid task raises an error
class TaskModelTest(TestCase):
    def test_create_valid_task(self):

        task = Task.objects.create(
            name="task1",
            planning_time="00:20:00",
            self_estimated_time="00:30:00",
            real_time_spent="00:50:00",
            complexity_level="EASY",
            risk_of_exceeding_time="OK",
            correctness=90,
            estimated_time_by_calc="00:30:00",
            notes="good",
        )

        self.assertTrue(isinstance(task, Task))

    def test_create_invalid_task_raise_error(self):

        with self.assertRaises(ValidationError):
            task = Task.objects.create(
                name="task1",
                planning_time="00:20:00",
                self_estimated_time="aaaaa",
                real_time_spent="00:50:00",
                complexity_level="EASY",
                risk_of_exceeding_time="OK",
                correctness=90,
                estimated_time_by_calc="00:30:00",
                notes="good",
            )


class UtilsTest(TestCase):
    def setUp(self):
        self.real_time = datetime.time(0, 10)
        self.estimated_time = datetime.time(0, 5)

    def test_time_in_sec(self):
        seconds = time_in_sec(self.real_time)
        self.assertEqual(seconds, 600)

    def test_wrong_time_in_sec(self):
        seconds = time_in_sec(self.real_time)
        self.assertNotEqual(seconds, 500)

    def test_get_correctness(self):
        correctness = get_correctness(self.real_time, self.estimated_time)
        self.assertEqual(correctness, 200)

    def test_wrong_get_correctness(self):
        correctness = get_correctness(self.real_time, self.estimated_time)
        self.assertNotEqual(correctness, 50)

    # todo: test_get_estimation_time


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("task_create_list")

    def test_get_task_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_create_list.html")

    # todo: test_post_task_view


class TestForm(TestCase):
    def test_valid_form(self):
        form_data = {
            "name": "task1",
            "planning_time": "00:20:00",
            "self_estimated_time": "00:30:00",
            "real_time_spent": "00:50:00",
            "complexity_level": "Easy",
            "risk_of_exceeding_time": "OK",
            "notes": "good",
        }
        form = CreateTask(data=form_data)
        self.assertTrue(form.is_valid())

    # todo: test_create_invalid_task_form_raise_validation_error


# TODO: Create tests for utils:
#   time_in_sec
#   get_correctness
#   get_estimation_time

# TODO: Create tests for Task model:
#   test_create_valid_task
#   test_create_invalid_task_raise_error

# TODO: Create tests for Task form:
#   test_create_valid_task_form
#   test_create_invalid_task_form_raise_validation_error

# TODO: Create test for views:
#   test_get_task_view: check for status code, return to the correct template
#   test_post_task_view: check for status code, redirect to the correct success url
