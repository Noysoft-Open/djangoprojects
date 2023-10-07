from django.urls import path

from . import views

urlpatterns = [
	path('polls/', views.index, name="polls-index"),
	path('polls/<int:question_id>/', views.detail, name='detail'),
	path('polls/<int:question_id>/results/', views.result, name='results'),
	path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]