from django.contrib import admin
from .models import *


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
	list_display = ('danish', 'spanish')
	list_filter = ('level', 'category')
	list_editable = ('spanish',)
	search_fields = ('spanish', 'danish')


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
	list_display = ('danish', 'spanish')
	list_filter = ('level',)
	list_editable = ('spanish',)


@admin.register(Top200Word)
class Top200WordAdmin(admin.ModelAdmin):
	list_display = ('spanish','danish', 'extra')


@admin.register(Expression)
class ExpressionAdmin(admin.ModelAdmin):
	list_display = ('spanish', 'danish', 'extra')
	list_editable = ('danish', 'extra')
	search_fields = ('spanish',)


@admin.register(Proverb)
class ProverbAdmin(admin.ModelAdmin):
	list_display = ('spanish', 'danish', 'extra')
	list_editable = ('danish', 'extra')
	search_fields = ('spanish',)


@admin.register(UserDeck)
class UserDeckAdmin(admin.ModelAdmin):
	list_display = ('navn', 'user')


admin.site.register([Category, UserWord])
