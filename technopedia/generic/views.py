from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# from user.models import CustomUser
from user.forms import UserForm
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login

# Create your views here.


class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'user/register.html'

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " - User Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:login')


class BaseAdminMixin(PermissionRequiredMixin):

    raise_exception = True
    permission_required = 'is_staff'
    redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

        if not self.has_permission():
            return redirect('/login-1/')
        return super(BaseAdminMixin, self).dispatch(request, *args, **kwargs)


class BaseCreateView(SuccessMessageMixin, CreateView, ListView):
    # model = CustomUser
    form_class = UserForm
    template_name = "user/User_creation.html"

    # def get_success_message(self, cleaned_data):
    #     self.name = cleaned_data['name']
    #     return self.name + " Created Successfully..!!"

    # def get_success_url(self):
    #     return reverse('user_urls:admin_customized')


class BaseUpdateView(SuccessMessageMixin, UpdateView):
    # model = CustomUser
    form_class = UserForm
    template_name = 'adminportal/update.html'
    # success_url = '/admin_customized/'

    def get_success_message(self, cleaned_data):
        self.name = cleaned_data["name"]
        return self.name + " Updated Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')


class BaseDeleteView(SuccessMessageMixin, DeleteView):
    # model = CustomUser
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_message(self, cleaned_data):
        return "Product Deleted Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')
