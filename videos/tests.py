from django.test import TestCase
from django.utils import timezone
from .models import Video
from djangoflix.db.models import PublishStateOptions

from django.utils.text import slugify
# Create your tests here.


class VideoModeTestCase(TestCase):
    def setUp(self):
        self.obj_a = Video.objects.create(
            title='This is a title', video_id='regs')
        self.obj_b = Video.objects.create(title='This is title', state=PublishStateOptions.PUBLISH,
                                          video_id='kjsjss')

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)

    def test_valid_title(self):
        title = 'This is a title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_account(self):
        qs = Video.objects.all()
        self.assertEqual(2, qs.count())

    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(1, qs.count())

    def test_publish_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Video.objects.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=now
        )

        self.assertTrue(published_qs.exists)

    def test_publish_manager(self):
        published_qs = Video.objects.all().published()
        published_qs_2 = Video.objects.published()
        self.assertTrue(published_qs.exists)
        self.assertEqual(published_qs.count(), published_qs_2.count())
