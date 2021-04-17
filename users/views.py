from django.shortcuts import render, HttpResponse
from users.user import User
from users import models


def index(request):

    userlist = models.User.objects.all()

    return render(
        request=request,
        template_name="index.html",
        context={"data": userlist},
    )


def add_user(request):
    if request.method == "GET":
        return render(
            request=request,
            template_name="add_user.html",
        )
    elif request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        user_ = User(username=username, email=email)

        user = models.User(
            username=user_.username,
            email=user_.email
        )
        user.save()

        return render(
            request=request,
            template_name="success.html",
            context={
                "username": user_.username,
                "email": user_.email,
            },
        )


def get_user(request, user_id):
    try:
        user_by_id = models.User.objects.get(id=user_id)
        return render(
            request=request,
            template_name="get_user.html",
            context={
                "username": user_by_id.username,
                "email": user_by_id.email,
            },
        )
    except models.User.DoesNotExist:
        return HttpResponse(f"User with ID:{user_id} does not exist in DB")


def edit_user(request, user_id):
    try:
        user_by_id = models.User.objects.get(id=user_id)
        if request.method == "GET":
            return render(
                request=request,
                template_name="add_user.html",
                context={
                    "username_value": user_by_id.username,
                    "email_value": user_by_id.email,
                },
            )

        if request.method == "POST":
            username = request.POST["username"]
            email = request.POST["email"]
            models.User.objects.filter(id=user_id).update(username=username, email=email)
            return render(
                request=request,
                template_name="get_user.html",
                context={
                    "username": username,
                    "email": email,
                }
            )
    except models.User.DoesNotExist:
        return HttpResponse(f"User with ID:{user_id} does not exist in DB")


def delete_user(request, user_id):
    try:
        user_by_id = models.User.objects.get(id=user_id)
        models.User.objects.filter(id=user_by_id.id).delete()
        return HttpResponse(f"Deleted <strong>{user_by_id.username}</strong> ")
    except models.User.DoesNotExist:
        return HttpResponse(f"User with ID:{user_id} does not exist in DB")
