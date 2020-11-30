from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.bibl_book, name='bibl_book'),
    path('create_bibl', views.create_bibl, name='create_bibl'),
    path('<int:pk>', views.BiblDetailView.as_view(), name='bibl-detail'),
    path('<int:pk>/updateb', views.BiblUpdateView.as_view(), name='bibl-update'),
    path('<int:pk>/deleteb', views.BiblDeleteView.as_view(), name='bibl-delete')

]