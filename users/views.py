from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy

from django.views.generic import (
    FormView,
    ListView,
    DetailView,
)

from django.views.generic.edit import (
    UpdateView,
    DeleteView
)

from users import (
    models,
    forms,
)
from users.forms import AddUserForm


# def index(request):
#
#     userlist = models.User.objects.all()
#
#     return render(
#         request=request,
#         template_name="user_list.html",
#         context={"data": userlist},
#     )


class UsersListView(ListView):
    model = models.User


# def add_user(request):
#     if request.method == "POST":
#
#         form = forms.AddUserForm(
#             data=request.POST,
#         )
#         if form.is_valid():
#             form.save()
#             return HttpResponse(f"<h1>Successfully added <u>{request.POST['username']}</u></h1><p>E-mail: {request.POST['email']} </p>")
#
#     else:
#         form = forms.AddUserForm()
#
#         return render(
#             request=request,
#             template_name="add_user.html",
#             context={
#                 "form": form,
#             },
#         )


class AddUser(FormView):
    template_name = "users/add_user.html"
    form_class = AddUserForm
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form=form)
        return response


# def get_user(request, user_id):
#     try:
#         user_by_id = models.User.objects.get(pk=user_id)
#         return render(
#             request=request,
#             template_name="users/user_detail.html",
#             context={
#                 "username": user_by_id.username,
#                 "email": user_by_id.email,
#             },
#         )
#     except models.User.DoesNotExist:
#         return HttpResponse(f"User with ID:{user_id} does not exist in DB")

class UserDetailView(DetailView):
    model = models.User

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["users"] = models.User.objects.filter(username=self.object)

        return context


# def edit_user(request, user_id):
#     try:
#         user = models.User.objects.get(pk=user_id)
#     except models.User.DoesNotExist:
#         return HttpResponse(f"User with ID:{user_id} does not exist in DB")
#
#     if request.method == "POST":
#         form = forms.AddUserForm(
#             data=request.POST,
#             instance=user,
#         )
#         if form.is_valid():
#             form.instance.save()
#             return HttpResponse(
#                 f"<h1>Successfully updated <u>{request.POST['username']}</u></h1><p>E-mail: {request.POST['email']} </p>")
#
#     else:
#         form = forms.AddUserForm(instance=user)
#         return render(
#             request=request,
#             template_name="users/add_user.html",
#             context={
#                 "form": form,
#             },
#         )


class EditUser(UpdateView):
    model = models.User
    fields = ["username", "email"]
    template_name_suffix = "_update_form"

# def delete_user(request, user_id):
#     try:
#         user = models.User.objects.get(pk=user_id)
#     except models.User.DoesNotExist:
#         return HttpResponse(f"User with ID:{user_id} does not exist in DB")
#
#     if request.method == "POST":
#         form = forms.DeleteUserForm(
#             data=request.POST,
#             instance=user,
#         )
#         if form.is_valid():
#             form.instance.delete()
#             return HttpResponse(
#                 f"<h1>Deleted <u>{request.POST['username']}</u></h1><p>E-mail: {request.POST['email']} </p>")
#
#     else:
#         form = forms.DeleteUserForm(instance=user)
#         return render(
#             request=request,
#             template_name="users/delete_user.html",
#             context={
#                 "form": form,
#             },
#         )


class DeleteUserView(DeleteView):
    model = models.User
    success_url = reverse_lazy('users')
