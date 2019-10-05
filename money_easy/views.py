from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import PayFor, PayItem
from .forms import SignupForm


# Create your views here.


def signup_func(request):
    if request.method == 'POST':
        input_username = request.POST['username']
        input_password = request.POST['password']
        try:
            User.objects.get(username=input_username)
            return render(request, 'registration/signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(input_username, '', input_password)
            return redirect('money_easy:login')
    return render(request, 'registration/signup.html', {})


def login_func(request):
    if request.method == 'POST':
        input_username = request.POST['username']
        input_password = request.POST['password']
        user = authenticate(request, username=input_username, password=input_password)
        if user is not None:
            login(request, user)
            return redirect('money_easy:pay_item_list')
        else:
            return render(request, 'registration/login.html', {'error': 'ユーザー名かパスワードが間違っています。もう一度入力してください。'})
    else:
        return render(request, 'registration/login.html')


@login_required()
def logout_func(request):
    logout(request)
    return redirect('money_easy:login')



# class SignupView(CreateView):
#     form_class = SignupForm
#     success_url = reverse_lazy('home')
#     template_name = 'registration/signup.html'
#
#     def form_valid(self, form):
#         # self.objectにsave()されたユーザーオブジェクトを格納
#         valid = super().form_valid(form)
#         login(self.request, self.object)
#         return valid


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'money_easy/index.html'


index = IndexView.as_view()


class PayForList(LoginRequiredMixin,ListView):
    template_name = 'money_easy/payfor_list.html'

    model = PayFor


pay_for_list = PayForList.as_view()



class PayForDetailView(LoginRequiredMixin, DetailView):
    template_name = 'money_easy/payfor_detail.html'

    model = PayFor


pay_for_detail = PayForDetailView.as_view()


class PayForCreate(LoginRequiredMixin,CreateView):
    template_name = 'money_easy/payfor_create.html'

    model = PayFor

    fields = ('name', 'description')
    success_url = reverse_lazy('money_easy:pay_item_list')


pay_for_create = PayForCreate.as_view()


class PayForDelete(LoginRequiredMixin, DeleteView):
    template_name = 'money_easy/payfor_delete.html'

    model = PayFor

    success_url = reverse_lazy('money_easy:pay_for_list')


pay_for_delete = PayForDelete.as_view()


class PayForUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'money_easy/payfor_update.html'

    model = PayFor

    fields = ('name', 'description')

    success_url = reverse_lazy('money_easy:pay_for_list')


pay_for_update = PayForUpdate.as_view()



class PayItemList(LoginRequiredMixin, ListView):
    template_name = 'money_easy/payitem_list.html'

    model = PayItem


pay_item_list = PayItemList.as_view()


class PayForDetailView(LoginRequiredMixin, DetailView):
    template_name = 'money_easy/payfor_detail.html'

    model = PayFor


payfor_detail = PayForDetailView.as_view()


class PayItemDetailView(LoginRequiredMixin, DetailView):
    template_name = 'money_easy/payitem_detail.html'

    model = PayItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['priority'] = PayItem.get_priority_display()
        return context


pay_item_detail = PayItemDetailView.as_view()


class PayItemCreate(LoginRequiredMixin,CreateView):
    template_name = 'money_easy/payitem_create.html'

    model = PayItem

    fields = ('title', 'payfor', 'money', 'rate', 'priority', 'duedate')
    success_url = reverse_lazy('money_easy:pay_item_list')


pay_item_create = PayItemCreate.as_view()


class PayItemDelete(LoginRequiredMixin, DeleteView):
    template_name = 'money_easy/payitem_delete.html'

    model = PayItem

    success_url = reverse_lazy('money_easy:pay_item_list')


pay_item_delete = PayItemDelete.as_view()


class PayItemUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'money_easy/payitem_update.html'

    model = PayItem

    fields = ('title', 'payfor', 'money', 'rate', 'priority', 'duedate')

    success_url = reverse_lazy('money_easy:pay_item_list')


pay_item_update = PayItemUpdate.as_view()

# class LoginView(AuthLoginView):
#     template_name = 'money_easy/login.html'
#
#
# login = LoginView.as_view()

# def hello(request):
#     if request.method == 'GET':
#         context = {
#             'message': 'Hello World',
#         }
#         return render(request, 'hello.html',context)
#
#
# class HelloView(View):
#     def get(self, request, *args, **kwargs):
#         context = {
#             'message': 'Hello World',
#         }
#         return render(request,'hello.html',context)
#
#
# hello = HelloView.as_view()
