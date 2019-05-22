from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    templates = 'home/home_page.html'
    max_count = 1

    banner_title = models.CharField(max_length=128, blank=False)
    banner_subtitle = RichTextField(featues=["bold", "italic"])

    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ]