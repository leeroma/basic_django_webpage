from django.urls import path

from webapp.views import Views

urlpatterns = [
    path('', Views.home_view, name='home'),
    path('one', Views.one_view, name='one'),
    path('two', Views.two_view, name='two'),
    path('three', Views.three_view, name='three'),
    path('four', Views.four_view, name='four'),
]
