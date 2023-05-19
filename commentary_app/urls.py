from django.urls import path

from commentary_app.views import (
    CommentListView,
    CommentCreateView,
    ReplyCommentCreateView,
)

app_name = "commentary_app"

urlpatterns = [
    path("", CommentListView.as_view(), name="comment_list"),
    path(
        "create-comment/", CommentCreateView.as_view(), name="create_comment"
    ),
    path(
        "create-reply-comment/<int:pk>/",
        ReplyCommentCreateView.as_view(),
        name="create_reply_comment",
    ),
]
