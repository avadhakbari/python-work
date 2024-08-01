#6]  Mention what command line can be used to load data into Django?

# >>>
# python manage.py loaddata: This command is used to load data from fixture files into your database.
# Fixture files are serialized representations of Django models, usually stored in JSON, XML, or YAML format. 
# The loaddata command can be used with the manage.py script in your Django project's root directory.
    
# python manage.py loaddata <fixture_file>
    
# python manage.py sqlsequencereset: This command is used to 
# display the SQL statements that reset the database's auto-incrementing sequences for a given app.
# It can be helpful when loading data that includes primary key fields and you want to ensure the 
# integrity of the auto-incrementing sequence.