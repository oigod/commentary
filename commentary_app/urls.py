from django.urls import path

from commentary_app.views import CommentListView

app_name = "commentary_app"

urlpatterns = [
    path("", CommentListView.as_view(), name="comment_list"),
]
