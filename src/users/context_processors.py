from django.http import HttpRequest


def user(request: HttpRequest) -> str:
    if request.session.get("user"):
        return {"username": request.session["user"]["userinfo"]["name"]}
    return {"username": None}
