from rest_framework.authtoken.models import Token


def create_auth_token(sender, instance=None, created=False, **kwargs):
    # Действие, рассчитанное на сигнал после создания записи пользователя.
    # Таким образом создаем ему автоматически токен.
    # Для этого нужно подключить rest_framework.authtoken в INSTALLED_APPS.
    if created:
        Token.objects.create(user=instance)


