from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


def validate_file_size(value):
    filesize = value.size
    if filesize > 100 * 1024:
        raise ValidationError(_("File size should not exceed 100 KB."))


class Comment(models.Model):
    """Model for comments"""

    username = models.CharField(max_length=255)
    email = models.EmailField()
    homepage = models.URLField(blank=True)
    text = models.TextField()
    parent_comment = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
    )
    image = models.ImageField(
        upload_to="comments/images/",
        validators=[
            FileExtensionValidator(["png", "jpg", "jpeg", "gif"]),
        ],
        blank=True,
    )
    file = models.FileField(
        upload_to="comments/files/",
        validators=[FileExtensionValidator(["txt"]), validate_file_size],
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.created_at}"

    class Meta:
        ordering = ("-created_at",)
