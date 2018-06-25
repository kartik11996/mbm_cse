from django.urls import path
from . import views

app_name='publications'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('publication/add/', views.PublicationCreate.as_view(), name='publication-add'),
    path('publication/update/', views.PublicationUpdate.as_view(), name='publication-update'),
    path('publication/delete/', views.PublicationDelete.as_view(), name='publication-delete'),

]