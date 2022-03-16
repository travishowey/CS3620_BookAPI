# Generated by Django 2.2 on 2022-03-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdata',
            name='book_image',
        ),
        migrations.AddField(
            model_name='bookdata',
            name='image',
            field=models.ImageField(default='images/none/noimg.jpg', upload_to='images'),
        ),
    ]