from . import dao
import magic
from api.exceptions.defines import WrongTypeException


def _format(user):
    if user:
        user_info = user.user_info
        result = dict(
            id=user.id,
            phone=user.phone,
            username=user.username,
            email=user.email,
            sex=user_info.sex,
            integral=user_info.integral,
            signature=user_info.signature,
            avatar=str(user_info.avatar)
        )
        return result


def get_profile(uid):
    user = dao.user.get_user(id=uid)
    return user

    return _format(user)


def update_profile(user, **kwargs):
    if kwargs.get('nickname'):
        nickname = kwargs.get('nickname')
        if dao.user_info.is_valid_nickname(nickname, user):
            dao.user_info.update(user, nickname=nickname)

    if kwargs.get('sex'):
        sex = kwargs.get('sex')
        dao.user_info.update(user, sex=sex)
    if kwargs.get('signature'):
        signature = kwargs.get('signature')
        dao.user_info.update(user, signature=signature)


def change_avatar(user, avatar):
    if not avatar:
        raise WrongTypeException('图片格式错误')
    file_info = magic.from_buffer(avatar.open('r').read(1024))
    if 'image' not in file_info:
        raise WrongTypeException('图片格式错误')
    user.user_info.avatar = avatar
    return user.user_info.save()

