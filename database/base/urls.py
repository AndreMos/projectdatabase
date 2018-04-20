from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    #url('', views.index, name='index'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/delete/', views.OrderDelete.as_view(), name='order_delete'),

    #rl(r'^$', views.index, name='index')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
