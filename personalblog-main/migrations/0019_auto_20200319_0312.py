# Generated by Django 3.0.4 on 2020-03-19 02:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0018_newslettersubcription_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsletterSubcription',
            new_name='NewsletterSubscription',
        ),
    ]
