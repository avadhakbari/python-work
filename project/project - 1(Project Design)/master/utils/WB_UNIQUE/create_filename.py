import os
import uuid

def generate_filename(instance, filename):
    # Get the filename and extension
    ext = filename.split('.')[-1]
    # Generate a unique filename
    filename = f'{str(uuid.uuid4())}_{instance.POSTFIX}.{ext}'
    # Return the path to upload the file
    return os.path.join(instance.DIR_NAME, filename)