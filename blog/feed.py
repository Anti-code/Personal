from django.contrib.syndication.views import Feed
from .models import Entry

class LatestPosts(Feed):
	"""docstring for LatestPosts"""
	title = "Python Snacks"
	link = "/feed/"
	description = "Latest Posts of Python Snacks"

	def items(self):
		return Entry.objects.published()[:3]