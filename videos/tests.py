from django.test import TestCase

from .models import Video
# Create your tests here.


class VideoModeTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title = 'This is a title')

    def test_valid_title(self):
        title = 'This is a title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())


    def test_created_account(self):
        qs = Video.objects.all()
        self.assertEqual(1, qs.count())