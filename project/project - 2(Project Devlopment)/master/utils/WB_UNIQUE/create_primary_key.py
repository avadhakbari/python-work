import uuid

def generate_primary_key(instance):
    primary_key = f'{str(uuid.uuid4())}_{instance.POSTFIX}'
    return primary_key