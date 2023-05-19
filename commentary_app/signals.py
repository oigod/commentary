import asyncio

from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

from .models import Comment


@receiver(post_save, sender=Comment)
def process_uploaded_photo(sender, instance, created, **kwargs):
    if created:
        if instance.image:
            max_width = 320
            max_height = 240

            image = Image.open(instance.image.path)

            if image.width > max_width or image.height > max_height:
                image.thumbnail((max_width, max_height), Image.ANTIALIAS)

            image.save(instance.image.path)


@receiver(post_save, sender=Comment)
def send_notification(sender, instance, created, **kwargs):
    from commentary_bot.bot import bot
    from commentary_bot.settings import settings

    if created:
        try:
            message = f"New comment was created by {instance.username}"
            asyncio.run(
                bot.send_message(chat_id=settings.NOTIFICATION_CHAT_ID, text=message)
            )
        except:
            pass
