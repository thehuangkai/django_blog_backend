from django.urls import include, path, re_path
from .views import portfolio_collection, portfolio_detail, PortfolioCreate


urlpatterns = [
    path('', portfolio_collection),
    path('create/', PortfolioCreate.as_view(), name='create-todo'),
    re_path(r'^(?P<portfolio_slug>[\w-]+)/$', portfolio_detail),
]