from django.views.generic import ListView

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, get_object_or_404

from .forms import CommentForm, ReplyCommentForm
from .models import Comment


class CommentListView(ListView):
    model = Comment
    template_name = "commentary_app/comment_list.html"
    context_object_name = "comments"
    paginate_by = 25
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get("sort")
        direction = self.request.GET.get(
            "dir", "asc"
        )  # Default direction is ascending

        if sort_by == "username":
            queryset = queryset.order_by(
                f'{"-" if direction == "desc" else ""}username'
            )
        elif sort_by == "email":
            queryset = queryset.order_by(
                f'{"-" if direction == "desc" else ""}email'
            )
        elif sort_by == "date":
            queryset = queryset.order_by(
                f'{"-" if direction == "desc" else ""}created_at'
            )

        return queryset


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "commentary_app/comment_create.html"
    success_url = reverse_lazy("commentary_app:comment_list")


class ReplyCommentCreateView(CreateView):
    model = Comment
    form_class = ReplyCommentForm
    template_name = "commentary_app/comment_reply_create.html"
    success_url = reverse_lazy("commentary_app:comment_list")

    def get_initial(self):
        initial = super().get_initial()
        initial["parent_comment"] = get_object_or_404(
            Comment, pk=self.kwargs["pk"]
        )
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment"] = get_object_or_404(Comment, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        parent = get_object_or_404(self.model, pk=self.kwargs["pk"])
        form.instance.parent_comment = parent
        return super().form_valid(form)
