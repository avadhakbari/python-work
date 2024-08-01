# 3] Explain what does django-admin.py make messages command is used for? 

# >>>

# Once you have marked the translatable strings, you can run the make messages command. It scans your codebase, including Python code,  templates, and configuration files, and extracts the marked strings into a language file called a "message file" or "PO file" (Portable Object file).
# After running the make messages command, you will have a set of PO files corresponding to different languages. These files contain the extracted translatable strings, along with their source and an empty target field for translations.

# You can distribute these PO files to translators who can then fill in the translations for each language. Translators can use tools like msgmerge or specialized translation software to edit PO files. 