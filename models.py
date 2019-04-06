from django.db import models
import uuid
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural= 'categories'


class Word(models.Model):
	danish = models.CharField(max_length=150)
	extra = models.CharField(max_length=200, blank=True)
	spanish = models.CharField(max_length=150)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	
	LEVELS = (
			('B', 'BEGINNER'),
			('I', 'INTERMEDIATE'),
			('A', 'ADVANCED')
		)

	level = models.CharField(max_length=1, choices=LEVELS, default='B')

	def __str__(self):
		return self.danish + ' | ' + self.spanish


class Phrase(models.Model):
	danish = models.CharField(max_length=500)
	spanish = models.CharField(max_length=500)
	
	LEVELS = (
			('B', 'BEGINNER'),
			('I', 'INTERMEDIATE'),
			('A', 'ADVANCED')
		)

	level = models.CharField(max_length=1, choices=LEVELS, default='B', null=True)

	def __str__(self):
		return self.spanish

class Expression(models.Model):
	spanish = models.CharField(max_length=250)
	danish = models.CharField(max_length=250)
	extra = models.CharField(max_length=250, blank=True)

	def __str__(self):
		return self.spanish


class Proverb(models.Model):
	spanish = models.CharField(max_length=250)
	danish = models.CharField(max_length=250)
	extra = models.CharField(max_length=250, blank=True)

	def __str__(self):
		return self.spanish


class Top200Word(models.Model):
	spanish = models.CharField(max_length=100)
	danish = models.CharField(max_length=100)
	extra = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.spanish


class UserDeck(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	navn = models.CharField(max_length=100)
	uuid = models. UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	def __str__(self):
		return self.navn


class UserWord(models.Model):
	spansk = models.CharField(max_length=250)
	dansk = models.CharField(max_length=250)
	user_deck = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.dansk + ' | ' + self.spansk
