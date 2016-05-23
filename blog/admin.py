from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
# Register your models here. https://www.google.com.tr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=7&cad=rja&uact=8&ved=0ahUKEwi7uuv_lrTMAhUJ3CwKHbHUAGIQFghDMAY&url=https%3A%2F%2Fgithub.com%2Fcjdd3b%2Fcitizen-quotes%2Fissues%2F1&usg=AFQjCNFdeYNxCQajmcrosVR0wORYse-Cvg&sig2=SM1ceWif-0cUAlEwBRkGcQ

class EntryAdmin(MarkdownModelAdmin):
	"""docstring for EntryAdmin"""
	list_display = ('title', 'publish_date')
	prepopulated_fields = {"slug":("title",)}

admin.site.register(models.Entry, MarkdownModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Author)
