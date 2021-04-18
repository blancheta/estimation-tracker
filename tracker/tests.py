from django.test import TestCase, Client
from django.urls import reverse, resolve
import json
from .models import *
from .views import *
import datetime
# Create your tests here.

class TestModels(TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		Task.objects.create(
			name = 'xx',
			planning = '07:04',
			estimate = '02:50',
			realtime = '04:52',
			risk = 'OK',
			level = 'easy',
			notes = 'azerty',
			estimateb_by_calc = '4:27',
			correctness = 50,
		)

	def test_Task(self):
		self.new = Task.objects.get(risk = 'OK',)
		self.assertEquals(self.new.realtime, datetime.time(4, 52))


class TestUrls(TestCase):
	"""docstring for ClassName"""
	def test_urls(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func.view_class, TaskView)


class TestView(TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		Task.objects.create(
			name = 'xxx',
			planning = '09:04',
			estimate = '07:50',
			realtime = '02:52',
			risk = 'OK',
			level = 'easy',
			notes = 'cool',
			estimateb_by_calc = '6:17',
			correctness = 50,
		)
		self.client = Client()
		self.url = reverse('home')



	def test_views_POST(self):
		self.post = Task.objects.get(name='xxx')
		self.assertEquals(self.post.risk, 'OK')



	def test_views_GET(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'tracker/home.html')
		