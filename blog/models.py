from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_markdown.models import MarkdownField
from django.utils.timezone import now
class Tag(models.Model):
	"""docstring for Tag"""
	slug = models.SlugField(max_length=140, unique=True)

	def __str__(self):
		return self.slug
		
class EntryQuerySet(models.QuerySet):
	"""docstring for EntryQuerySet"""
	def published(self):
		return self.filter(publish=True)

class Author(models.Model):
	"""docstring for Author"""
	picture = models.ImageField(upload_to="")
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	expertise = models.TextField(max_length=200)
	info = models.TextField(max_length=200)
	identy = "Mehmet Gürdal"
	def __str__(self):
		return self.identy


		
class Comment():
	"""docstring for Comment"""
	firs_name = models.CharField(max_length=140, default=None)
	last_name = models.CharField(max_length=140, default= None)
	date = models.DateTimeField(auto_now_add = True)
	#reply = models.ManyToManyField('blog.models.Comment', related_name="reply")
	post = models.ForeignKey('blog.models.Entry')
	def __str__(self):
		return self.firs_name+" "+self.last_name


class Entry(models.Model):
	"""docstring for Entry"""
	picture = models.ImageField(upload_to="",default=None, blank=True, null=True)
	title = models.CharField(max_length=140)
	info = models.CharField(max_length=140)
	body = MarkdownField()
	author_comment = MarkdownField(default=None, blank=True, null=True)
	source_code = models.URLField(default=None, blank=True, null=True)
	tags = models.ManyToManyField(Tag, related_name="tags")
	author = models.ManyToManyField(Author, related_name="author")
	objects = EntryQuerySet.as_manager()
	publish = models.BooleanField(default=True)
	slug = models.SlugField(max_length=140, unique=True)
	publish_date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("entry_detail", kwargs = {"slug":self.slug})

	class Meta(object):
		"""docstring for Meta"""
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"		
		ordering = ["-publish_date"]



		