from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


UserModel = get_user_model()


def create_user_if_not_exist(
    *,
    email: str,
    first_name: str,
    last_name: str,
) -> None:
    if UserModel.objects.filter(email=email).exists():
        return

    password = make_password(password=None)

    user = UserModel(
        username=email,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )
    user.save()
