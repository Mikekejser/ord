from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *
import random
from django.contrib import messages


def main(request):
	return render(request, 'ord/main.html')


def alle_ord(request):
	if request.method == 'POST':
		search_input = request.POST.get('search-field', None)
		if len(search_input) >= 3:
			words = Word.objects.filter(spanish__icontains=search_input)
		else:
			words = Word.objects.filter(spanish=search_input)
		return render(request, 'ord/alle_ord.html', {'words': words})
	return render(request, 'ord/alle_ord.html')


def kategorier(request):
	categories = Category.objects.order_by('name')
	return render(request, 'ord/kategorier.html', {'categories': categories})


def kategori(request, name, level):
	category = get_object_or_404(Category, name=name)
	if level == 'alle':
		words = get_list_or_404(Word, category=category)
	elif level == 'let':
		words = get_list_or_404(Word, category=category, level='B')
	elif level == 'øvet':
		words = get_list_or_404(Word, category=category, level='I')
	else:
		words = get_list_or_404(Word, category=category, level='A')
	return render(request, 'ord/kategori.html', {'words': words, 'name': name, 'category': category})


def top_200(request):
	random10 = random.sample(range(1,201), 10)
	words = Top200Word.objects.filter(id__in=random10)
	return render(request, 'ord/top_200.html', {'words': words})


def fraser(request, level):
	if level == 'alle':
		my_ids = Phrase.objects.all().values_list('id', flat=True)
		my_ids = list(my_ids)
		random5_ids = random.sample(my_ids, 5)
		phrases = Phrase.objects.filter(id__in=random5_ids)
	elif level == 'let':
		my_ids = Phrase.objects.filter(level='B').values_list('id', flat=True)
		my_ids = list(my_ids)
		random5_ids = random.sample(my_ids, 5)
		phrases = Phrase.objects.filter(id__in=random5_ids)
	elif level == 'øvet':
		my_ids = Phrase.objects.filter(level='I').values_list('id', flat=True)
		my_ids = list(my_ids)
		random5_ids = random.sample(my_ids, 5)
		phrases = Phrase.objects.filter(id__in=random5_ids)
	else:
		my_ids = Phrase.objects.filter(level='A').values_list('id', flat=True)
		my_ids = list(my_ids)
		random5_ids = random.sample(my_ids, 5)
		phrases = Phrase.objects.filter(id__in=random5_ids)
		
	return render(request, 'ord/fraser.html', {'phrases': phrases})


def udtryk(request):
	my_ids = Expression.objects.all().values_list('id', flat=True)
	my_ids = list(my_ids)
	random5_ids = random.sample(my_ids, 5)
	expressions = Expression.objects.filter(id__in=random5_ids)
	return render(request, 'ord/udtryk.html', {'expressions': expressions})


def ordsprog(request):
	my_ids = Proverb.objects.all().values_list('id', flat=True)
	my_ids = list(my_ids)
	random5_ids = random.sample(my_ids, 5)
	proverbs = Proverb.objects.filter(id__in=random5_ids)
	return render(request, 'ord/ordsprog.html', {'proverbs': proverbs})
