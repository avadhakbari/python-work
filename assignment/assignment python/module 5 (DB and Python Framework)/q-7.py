#7] Explain what does django-admin.py make messages command is used for? 

# >>>
# The django-admin.py make messages command is used in Django to generate language translation files based on the text strings in your
# Django project. These translation files can then be used to localize your application and provide translations for different languages.

# When you run the make messages command, Django looks for text strings wrapped in translation functions or tags throughout your project's 
#     source code, templates, and other files. These translation functions or tags are typically gettext or ugettext functions or the
# {% trans %} template tag.

# Django extracts these text strings and creates or updates a set of message files, known as "PO" files (Portable Object files). Each PO 
# file corresponds to a specific language and contains the original text strings and their translations, if available.

# Once the PO files are generated, you or a translator can open them and provide translations for each text string in the desired language. 
# The translations are added as entries in the PO files, and each entry consists of the original string and its translated version.

# After the translations are added, you can use Django's localization features to load the appropriate translation files based on the user's 
# preferred language. This allows your application to display the text strings in the user's language, making it more accessible and 
# user-friendly for people from different regions.

# Overall, the django-admin.py make messages command is an essential tool in the localization process of a Django project, helping you 
# extract text strings for translation and manage the translation workflow efficiently.