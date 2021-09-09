from django.db import models

from wagtail.core.models import Page

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtailcloudinary.fields import CloudinaryField, CloudinaryWidget
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtailcloudinary.blocks import CloudinaryImageBlock
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


class HomePage(Page):
    title_image = CloudinaryField('title_image', null=True, blank=True)
    logo = CloudinaryField('logo', null=True, blank=True)

    slider = StreamField([
        ('image', CloudinaryImageBlock()),
        ('link', blocks.CharBlock())
    ], null=True, blank=True)
    # carusel
    # text (whole in struct block)
    # icon 
    # link

    selection_1_image = CloudinaryField('selection_1_image', null = True, blank = True)
    selection_1_text = RichTextField(null=True, blank=True)

    selection_2_image = CloudinaryField('selection_2_image', null = True, blank = True)
    selection_2_text = RichTextField(null=True, blank=True)

    # form
    email_reciver = models.CharField(blank=True, null=True, max_length=255)
    
    content_panels = Page.content_panels + [
        FieldPanel('title_image', widget=CloudinaryWidget),
        FieldPanel('logo', widget=CloudinaryWidget),
        StreamFieldPanel('slider'),
        FieldPanel('selection_1_text'),
        FieldPanel('selection_1_image', widget=CloudinaryWidget),
        FieldPanel('selection_2_text'),
        FieldPanel('selection_2_image', widget=CloudinaryWidget),
        FieldPanel('email_reciver'),
    ]

