from django.urls import path

from .views import index, signup_func, login_func, logout_func, pay_for_list,pay_for_create,pay_for_detail,pay_for_delete,pay_for_update,payfor_detail, pay_item_detail, pay_item_list, pay_item_create, pay_item_delete, pay_item_update

app_name = 'money_easy'
urlpatterns = [
    # path('login/',views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('', index, name='index'),
    path('signup/', signup_func, name='signup'),
    path('login/', login_func, name='login'),
    path('logout/', logout_func, name='logout'),
    path('payforlist/', pay_for_list, name='pay_for_list'),
    path('payfor/<int:pk>', pay_for_detail, name='pay_for_detail'),
    path('payforcreate/', pay_for_create, name='pay_for_create'),
    path('payfordelete/<int:pk>', pay_for_delete, name='pay_for_delete'),
    path('payforupdate/<int:pk>', pay_for_update, name='pay_for_update'),
    path('payitemlist/',pay_item_list, name='pay_item_list'),
    path('payitem/<int:pk>', pay_item_detail, name='pay_item_detail'),
    path('payitemcreate/', pay_item_create, name='pay_item_create'),
    path('payitemdelete/<int:pk>', pay_item_delete, name='pay_item_delete'),
    path('payitemupdate/<int:pk>', pay_item_update, name='pay_item_update'),
]
