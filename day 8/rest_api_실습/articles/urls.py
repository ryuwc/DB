from django.urls import path
from . import views

urlpatterns = [
    # 게시글 전체 조회 => GET     /api/v1/articles/
    # 게시글 생성 =>      POST    /api/v1/articles/
    path('articles/', views.article_list),

    # 상세글 조회 =>      GET     /api/v1/articles/1/
    # 상세글 삭제 =>      DELETE  /api/v1/articles/1/ 
    # 상세글 수정 =>      PUT     /api/v1/articles/1/ 
    path('articles/<int:article_pk>/', views.article_detail),

    # 댓글 전체 조회 => Get       /api/v1/comments/
    path('comments/', views.comment_list),

    # 댓글 상세 조회 => GET       /api/v1/comments/1/
    # 댓글 수정 => PUT            /api/v1/comments/1/
    # 댓글 삭제 => DELETE         /api/v1/comments/1/
    path('comments/<int:comment_pk>/', views.comment_detail),

    # 댓글 생성 => POST           /api/v1/articles/1/comments/
    path('articles/<int:article_pk>/comments/', views.comment_create),

]
