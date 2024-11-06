from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *



def main_page(request):

	return render(request, 'main/main_page.html',)