from api.models import IdentityCode
from django.db.models import Q
import time
from common.utils import current_timestamp


def create(**kwargs):
    identity_code = IdentityCode.objects.create(**kwargs)
    identity_code.save()
    return identity_code


def is_valid_code(phone, code, template_code):
    now = current_timestamp()
    return IdentityCode.objects.filter(phone=phone, code=code, template_code=template_code, expire_at__gt=now).exists()



