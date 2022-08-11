from django.http import HttpRequest


def user(request: HttpRequest) -> str:
    if request.user.is_authenticated:
        return {"username": request.user.username}
    return {"username": None}
