from django.urls import path
from .views import simpleCreate,simpleListView,simpleDetailView,simpleUpdateView,simpleDeleteView

urlpatterns = [
    path('create/', simpleCreate.as_view(), name='create'),
    path('list/',simpleListView.as_view(), name='list'),
    path('detail/<int:pk>/',simpleDetailView.as_view(), name='detail'),
    path('update/<int:pk>/',simpleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',simpleDeleteView.as_view(), name='delete'),
]
