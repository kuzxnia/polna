# Generated by Django 3.1.2 on 2020-11-26 19:59

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='selection_1_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='selection_1_text',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='selection_2_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='selection_2_text',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
