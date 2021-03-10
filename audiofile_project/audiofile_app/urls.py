from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.audio_book_list, name='audio_book_list'),
    path('add/', views.audio_book_form, name='audio_book_add'),
    path('<int:audio_book_id>/detail/', views.audio_book_detail, name='audio_book_detail'),
    path('<int:id>/update/', views.audio_book_form, name='audio_book_update'),
    path('<int:audio_book_id>/delete/', views.audio_book_delete, name='audio_book_delete'),

]
