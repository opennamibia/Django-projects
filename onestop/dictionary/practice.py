from .forms import SearchWordForm, EnglishWordForm, OshindongaWordForm, WordDefinitionForm, DefinitionExampleForm

# TEST SEARCH FUNCTIONS
# context = {'form': '', 'searched_word': '',
#            'definitions': '', 'examples': ''}


# def search_examples(request, definitions_pks):
#     '''
#         Takes in a list of pks of found definitions and search if examples exist and return example objects.
#     '''
#     example_querysets = []
#     for definition_pk in definitions_pks:
#         example_queryset = DefinitionExample.objects.filter(
#             definition_id=definition_pk)
#         # If no definition found, an empty queryset is appended
#         example_querysets.append(example_queryset)
#     # print(example_querysets)
#     # print(len(example_querysets))
#     example_objects = []
#     no_example_found = 'No example found'
#     for example_queryset in example_querysets:
#         if len(example_queryset) > 0:  # If it's not an empty querset
#             # Loop through the queryset to extract objects
#             for i in range(len(example_queryset)):
#                 example_objects.append(example_queryset[i])
#         else:
#             example_objects.append(no_example_found)
#     context['examples'] = example_objects
#     # print('Example objects: %s' % example_objects)
#     return render(request, 'dictionary/search.html', context)


# def search_definitions(request, word_pairs_pks):
#     '''
#         Takes in a list pks of word pairs and return a list of pks of all definitions found.
#     '''
#     sub_request3 = request
#     definition_querysets = []
#     for pair_pk in word_pairs_pks:
#         definition_queryset = WordDefinition.objects.filter(
#             word_pair_id=pair_pk)
#         # If no definition found, an empty queryset is appended
#         definition_querysets.append(definition_queryset)
#     # print(definition_querysets)
#     # print(len(definition_querysets))
#     definition_objects = []
#     no_definition_found = 'No definition found'
#     for definition_queryset in definition_querysets:
#         if len(definition_queryset) > 0:  # If it's not an empty queryset
#             for i in range(len(definition_queryset)):
#                 definition_objects.append(definition_queryset[i])
#         else:
#             definition_objects.append(no_definition_found)
#     context['definitions'] = definition_objects
#     # print('Cleaned definitions: %s' % definition_objects)
#     definitions_pks = []
#     for i in range(len(definition_objects)):
#         if definition_objects[i] != no_definition_found:
#             definitions_pks.append(definition_objects[i].id)
#     # print(definitions_pks)
#     # return definitions_pks
#     search_examples(sub_request3, definitions_pks)


# def search_word_pairs(request, eng_word_pk):
#     '''
#         Using the English word pk (foreignkey id) search if for English|Oshindonga pairs and return a list of pks of all pair objects found.
#     '''
#     sub_request2 = request
#     # Return a queryset of all word pairs with the searched word
#     word_pairs = OshindongaWord.objects.filter(english_word_id=eng_word_pk)
#     print('Word_pairs1: %s' % word_pairs)
#     print(len(word_pairs))
#     if len(word_pairs) == 0:
#         print('Word_pairs2: %s' % word_pairs)
#         context['searched_word'] = [
#             'The word you searched is not yet translated into Oshindonga.']
#         return render(request, 'dictionary/search.html', context)
#     else:
#         context['searched_word'] = word_pairs
#         # Etract pk/id of each pair and save them in a list
#         word_pairs_pks = [
#             word_pair.id for word_pair in word_pairs]
#         # return word_pairs_pks
#         search_definitions(sub_request2, word_pairs_pks)


# def search_word(request):
#     '''
#         Check if the searched English word exists in the English model. If found return its pk
#     '''
#     sub_request = request
#     # print('Started here')
#     # Reset context variables when visiting for the first time or refreshing the page
#     # context['form'] = SearchWordForm()
#     context['searched_word'] = ''
#     context['definitions'] = ''
#     context['examples'] = ''
#     form = SearchWordForm(request.GET)
#     context['form'] = form
#     # print(form)
#     # print(form.is_valid())
#     if form.is_valid():
#         # print('Passed here')
#         word = form.cleaned_data['search_word']
#         try:
#             # Search within English model, and if foud:
#             eng_word = EnglishWord.objects.get(word=word)
#             # Get the the id/pk of the word found to be used in Oshindonga model
#             eng_word_pk = eng_word.id
#         except EnglishWord.DoesNotExist:
#             return render(request, 'dictionary/search.html', context)
#         search_word_pairs(sub_request, eng_word_pk)
#         return render(request, 'dictionary/search.html', context)
#     else:
#         return render(request, 'dictionary/search.html', context)

app_name = 'dictionary'
urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search_word, name='search'),
    path('add_english', views.add_english, name='add-english'),
    path('add_oshindonga', views.add_oshindonga, name='add-oshindonga'),
    path('add_definition', views.add_definition, name='add-definition'),
    path('add_example', views.add_example, name='add-example'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('english-word/<int:pk>/update/',
         views.EnglishWordUpdate.as_view(), name='english-word-update'),
    path('oshindonga-word/<int:pk>/update/',
         views.OshindongaWordUpdate.as_view(), name='oshindonga-word-update'),
    path('definition/<int:pk>/update/',
         views.WordDefinitionUpdate.as_view(), name='word-definition-update'),
    path('example/<int:pk>/update/', views.DefinitionExampleUpdate.as_view(),
         name='definition-example-update'),
]



    #     path('english', views.add_english, name='add-english'),
    #     path('oshindonga', views.add_oshindonga, name='add-oshindonga'),
    #     path('definition', views.add_definition, name='add-definition'),
    #     path('example', views.add_example, name='add-example'),

    {% url 'dictionary:english' %}


    
# def add_english(request):
#     if request.method == 'POST':
#         form = EnglishWordForm(request.POST)
#         if form.is_valid():
#             new_word = form
#             new_word.save()
#             return HttpResponseRedirect(reverse('dictionary:add-english'))
#     else:
#         form = EnglishWordForm()
#     return render(request, 'dictionary/add_english.html/', {'form': form, 'operation': 'Add new English word'})


# def add_oshindonga(request):
#     if request.method == 'POST':
#         form = OshindongaWordForm(request.POST)
#         if form.is_valid():
#             new_word = form
#             new_word.save()
#             return HttpResponseRedirect(reverse('dictionary:add-oshindonga'))
#     else:
#         form = OshindongaWordForm()
#     return render(request, 'dictionary/add_oshindonga.html/', {'form': form})


# def add_definition(request):
#     if request.method == 'POST':
#         form = WordDefinitionForm(request.POST)
#         if form.is_valid():
#             new_definition = form
#             new_definition.save()
#             return HttpResponseRedirect(reverse('dictionary:add-definition'))
#     else:
#         form = WordDefinitionForm()
#     return render(request, 'dictionary/add_definition.html/', {'form': form})


# def add_example(request):
#     if request.method == 'POST':
#         form = DefinitionExampleForm(request.POST)
#         if form.is_valid():
#             new_definition = form
#             new_definition.save()
#             return HttpResponseRedirect(reverse('dictionary:add_example'))
#     else:
#         form = DefinitionExampleForm()
#     return render(request, 'dictionary/add_example.html/', {'form': form})