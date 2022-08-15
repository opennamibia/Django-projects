from dictionary.models import WordDefinition


def update_pos():
    print("Running update query...")
    WordDefinition.objects.filter(part_of_speech="noun").update(part_of_speech="NOUN")
    WordDefinition.objects.filter(part_of_speech="Noun").update(part_of_speech="NOUN")
    WordDefinition.objects.filter(part_of_speech="Noun [C]").update(
        part_of_speech="NOUN"
    )
    WordDefinition.objects.filter(part_of_speech="Noun [C]").update(
        part_of_speech="NOUN"
    )
    WordDefinition.objects.filter(part_of_speech="adjective").update(
        part_of_speech="ADJ"
    )
    WordDefinition.objects.filter(part_of_speech="adposition").update(
        part_of_speech="ADP"
    )
    WordDefinition.objects.filter(part_of_speech="adverb").update(part_of_speech="ADV")
    WordDefinition.objects.filter(part_of_speech="auxiliary").update(
        part_of_speech="AUX"
    )
    WordDefinition.objects.filter(part_of_speech="coordinating conjunction").update(
        part_of_speech="CCONJ"
    )
    WordDefinition.objects.filter(part_of_speech="determiner").update(
        part_of_speech="DET"
    )
    WordDefinition.objects.filter(part_of_speech="interjection").update(
        part_of_speech="INTJ"
    )
    WordDefinition.objects.filter(part_of_speech="numerical").update(
        part_of_speech="NUM"
    )
    WordDefinition.objects.filter(part_of_speech="particle").update(
        part_of_speech="PART"
    )
    WordDefinition.objects.filter(part_of_speech="pronoun").update(
        part_of_speech="PRON"
    )
    WordDefinition.objects.filter(part_of_speech="Proper noun").update(
        part_of_speech="PROPN"
    )
    WordDefinition.objects.filter(part_of_speech="subordinating conjunction").update(
        part_of_speech="SCONJ"
    )
    WordDefinition.objects.filter(part_of_speech="verb").update(part_of_speech="VERB")
    WordDefinition.objects.filter(part_of_speech="Verb").update(part_of_speech="VERB")
    print("Update finished!")
