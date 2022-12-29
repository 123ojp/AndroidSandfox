

from django.core.exceptions import PermissionDenied
def required_membership():
    def inner(view_func):
        def wrapper(request, *args, **kwargs):
            team_id = kwargs['team_id']
            team = Team.objects.get(pk=team_id)
            if team.has_user(request.user.id):
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrapper

    return inner

import os,shutil, string, random
def id_generator(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()