from django.views.generic import ListView
from .models import Comment


class CommentListView(ListView):
    model = Comment
    template_name = "commentary_app/comment_list.html"
    context_object_name = "comments"
