from django.db import models

from wagtail.core.models import Page

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class HomePage(Page):
    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # carusel
    # text (whole in struct block)
    # icon 
    # link

    selection_1_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selection_1_text = RichTextField(
        null=True,
        blank=True,

    )
    selection_2_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    selection_2_text = RichTextField(
        null=True,
        blank=True,
    )


    # form
    email_reciver = models.CharField(blank=True, null=True, max_length=255)
    
    content_panels = Page.content_panels + [
        FieldPanel('title_image'),
        FieldPanel('selection_1_text'),
        FieldPanel('selection_1_image'),
        FieldPanel('selection_2_text'),
        FieldPanel('selection_2_image'),
        FieldPanel('email_reciver'),
    ]


#  
