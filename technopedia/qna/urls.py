from django.urls import path
from qna import views

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='quelist'),
    path('myque/', views.UserQuestionListView.as_view(), name='userquelist'),
    path('add/', views.AddQue.as_view(), name='addque'),
    path('update/<int:pk>', views.QuestionUpdateView.as_view(), name="queupdate"),
    path('delete/<int:pk>', views.QuestionDeleteView.as_view(), name="quedelete"),
    path('detail/<id>', views.QdetailView.as_view(), name="quedetail"),
    path('supdate/<int:pk>', views.StatusUpdateView.as_view(), name="stupdate"),
    path('like/<int:pk>', views.AddLike.as_view(), name="like_post"),
    path('dislike/<int:pk>', views.DislikeView.as_view(), name="dislike_post"),
    path('search/', views.QuestionSearch.as_view(), name="search_question"),
]
