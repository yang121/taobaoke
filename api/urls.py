"""taobaoke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from api import views

urlpatterns = [
    path('item/', views.ItemView.as_view()),
    # path('item/<str:q>/<str:cat>/<str:itemloc>/<str:sort>/<str:is_tmall>/<str:is_overseas>/<int:start_price>/<int:end_price>/<int:start_tk_rate>/<int:end_tk_rate>/<int:platform>/<int:page_no>/', views.get_item),
]