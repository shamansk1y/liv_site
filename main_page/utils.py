import os
from datetime import datetime


def get_file_name(instance, filename):
    ext = filename.strip().split('.')[-1]
    now = datetime.now()
    folder_name = f'{now.year}/{now.month:02d}'
    new_file_name = f'{instance.slug}.{ext}'
    return os.path.join(instance.__class__.__name__.lower(), folder_name, new_file_name)


def get_file_name_id(instance, filename):
    ext = filename.strip().split('.')[-1]
    now = datetime.now()
    folder_name = f'{now.year}/{now.month:02d}'
    new_file_name = f'{instance.id}.{ext}'
    return os.path.join(instance.__class__.__name__.lower(), folder_name, new_file_name)