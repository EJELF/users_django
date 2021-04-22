from django.shortcuts import render, HttpResponse
from users import (
    models,
    forms,
)


def index(request):

    userlist = models.User.objects.all()

    return render(
        request=request,
        template_name="index.html",
        context={"data": userlist},
    )


def add_user(request):
    if request.method == "POST":

        form = forms.AddUserForm(
            data=request.POST,
        )
        if form.is_valid():
            form.save()
            return HttpResponse(f"<h1>Successfully added <u>{request.POST['username']}</u></h1><p>E-mail: {request.POST['email']} </p>")

    else:
        form = forms.AddUserForm()

        return render(
            request=request,
            template_name="add_user.html",
            context={
                "form": form,
            },
        )


def get_user(request, user_id):
    try:
        user_by_id = models.User.objects.get(pk=user_id)
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
        user = models.User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return HttpResponse(f"User with ID:{user_id} does not exist in DB")

    if request.method == "POST":
        form = forms.AddUserForm(
            data=request.POST,
            instance=user,
        )
        if form.is_valid():
            form.instance.save()
            return HttpResponse(
                f"<h1>Successfully updated <u>{request.POST['username']}</u></h1><p>E-mail: {request.POST['email']} </p>")

    else:
        form = forms.AddUserForm(instance=user)
        return render(
            request=request,
            template_name="add_user.html",
            context={
                "form": form,
            },
        )

    # try:
    #     user_by_id = models.User.objects.get(id=user_id)
    #     if request.method == "GET":
    #         return render(
    #             request=request,
    #             template_name="add_user.html",
    #             context={
    #                 "username_value": user_by_id.username,
    #                 "email_value": user_by_id.email,
    #             },
    #         )
    #
    #     if request.method == "POST":
    #         username = request.POST["username"]
    #         email = request.POST["email"]
    #         models.User.objects.filter(id=user_id).update(username=username, email=email)
    #         return render(
    #             request=request,
    #             template_name="get_user.html",
    #             context={
    #                 "username": username,
    #                 "email": email,
    #             }
    #         )
    # except models.User.DoesNotExist:
    #     return HttpResponse(f"User with ID:{user_id} does not exist in DB")


def delete_user(request, user_id):
    try:
        user = models.User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return HttpResponse(f"User with ID:{user_id} does not exist in DB")

    if request.method == "POST":
        form = forms.DeleteUserForm(
            data=request.POST,
            instance=user,
        )
        if form.is_valid():
            form.instance.delete()
            return HttpResponse(
                f"<h1>Deleted <u>{request.POST['username']}</u></h1><p>E-mail: {request.POST['email']} </p>")

    else:
        form = forms.DeleteUserForm(instance=user)
        return render(
            request=request,
            template_name="delete_user.html",
            context={
                "form": form,
            },
        )
