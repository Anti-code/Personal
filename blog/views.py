from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from . import models
from django.views.generic import ListView, DetailView

class BlogIndex(ListView):
	"""docstring for BlogIndex"""
	queryset = models.Entry.objects.published()
	template_name = "index.html"
	paginate_by = 5

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(BlogIndex, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['authors'] = models.Author.objects.all()
		

		return context
	
class BlogDetail(DetailView):
	"""docstring for BlogIndex"""
	#model = models.Entry
	template_name = "blog-single.html"
	model = models.Entry
	

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(BlogDetail, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		#context['authors'] = models.Author.objects.all()
		context['tags']= models.Tag.objects.filter(tags=self.model.id)
		return context
	
class Portfolio(ListView):
	"""docstring for Portfolio"""
	queryset = models.Entry.objects.published()
	template_name = "portfolio.html"
	paginate_by = 10

class About(ListView):
	"""docstring for About"""
	queryset=models.Author.objects.all()
	template_name = "about.html"
