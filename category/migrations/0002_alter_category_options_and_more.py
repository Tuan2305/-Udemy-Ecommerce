# Generated by Django 4.2 on 2023-06-02 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_img',
            new_name='category_image',
        ),
    ]