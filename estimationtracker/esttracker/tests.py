import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.test.client import Client
from django.urls import resolve, reverse

from .forms import CreateTask
from .models import *
from .utils import (
    calculate_correctness_ratio,
    get_estimation_time_by_calc,
    convert_time_to_seconds,
)
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
        self.assertEquals(1, Task.objects.all().count())

    def test_create_invalid_task_raise_error(self):

        with self.assertRaises(ValidationError) as err:
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

        self.assertRaisesMessage(err, "“aaaaa” value has an in[53 chars]t.")


class UtilsTest(TestCase):
    def setUp(self):
        self.real_time = datetime.time(0, 10)
        self.estimated_time = datetime.time(0, 5)

    def test_convert_time_to_seconds(self):
        seconds = convert_time_to_seconds(self.real_time)
        self.assertEquals(seconds, 600)

    def test_convert_time_to_seconds_raise_value_error(self):
        with self.assertRaises(ValueError) as err:
            seconds = convert_time_to_seconds(0)

    def test_calculate_correctness_ratio(self):
        correctness = calculate_correctness_ratio(self.real_time, self.estimated_time)
        self.assertEquals(correctness, 200)

    def test_calculate_correctness_ratio_raise_type_error(self):
        with self.assertRaises(TypeError) as err:
            correctness = calculate_correctness_ratio(self.real_time)

    def test_get_estimation_time_by_calc_no_tasks(self):
        """
        It checks if returns None when there is no tasks in the database
        """

        estimation_time_by_calc = get_estimation_time_by_calc(self.estimated_time)
        self.assertEquals(estimation_time_by_calc, None)

    def test_get_estimation_time_by_calc(self):
        """
        It checks if calculation is correct when there is one task in the database
        """
        task = Task.objects.create(
            name="task1",
            planning_time="00:20:00",
            self_estimated_time="00:40:00",
            real_time_spent="00:50:00",
            complexity_level="EASY",
            risk_of_exceeding_time="OK",
            correctness=80,
            notes="good",
        )

        estimation_time_by_calc = get_estimation_time_by_calc(self.estimated_time)
        self.assertEquals(estimation_time_by_calc, "0:04:00")


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("task_create_list")

    def test_get_task_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_create_list.html")

    # todo: test_post_task_view
    def test_post_task_view(self):
        response = self.client.post(
            self.url,
            data={
                "name": "test_post_task_view",
                "planning_time": "00:20:00",
                "self_estimated_time": "00:30:00",
                "real_time_spent": "00:50:00",
                "complexity_level": "Easy",
                "risk_of_exceeding_time": "OK",
                "notes": "good",
            },
        )

        self.assertEquals("test_post_task_view", Task.objects.last().name)
        self.assertEquals(response.status_code, 302)


# git checkout -b fix-comments
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

    def test_create_invalid_form(self):
        form_data = {
            "name": "task1",
            "planning_time": "00:20:00",
            "self_estimated_time": "00:30:00",
            "real_time_spent": "00:50:00",
            "complexity_level": "Easy1",
            "risk_of_exceeding_time": "OK",
            "notes": "good",
        }
        form = CreateTask(data=form_data)
        self.assertEquals(
            "Select a valid choice. Easy1 is not one of the available choices.",
            form.errors["complexity_level"][0],
        )

    # todo: test_create_invalid_task_form_raise_validation_error


# TODO: Create tests for utils:
#   time_in_sec
#   calculate_correctness_ratio
#   get_estimation_time_by_cal

# TODO: Create tests for Task model:
#   test_create_valid_task
#   test_create_invalid_task_raise_error

# TODO: Create tests for Task form:
#   test_create_valid_task_form
#   test_create_invalid_task_form_raise_validation_error

# TODO: Create test for views:
#   test_get_task_view: check for status code, return to the correct template
#   test_post_task_view: check for status code, redirect to the correct success url
