# Generated by Django 3.2 on 2021-06-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210620_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_quotes', models.TextField(blank=True, max_length=999, null=True)),
                ('footer_contact_title', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('footer_links_title', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_payment_title', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_facebook_link', models.URLField(blank=True, max_length=999, null=True)),
                ('footer_instagram_link', models.URLField(blank=True, max_length=999, null=True)),
                ('footer_twitter_link', models.URLField(blank=True, max_length=999, null=True)),
                ('footer_linkedin_link', models.URLField(blank=True, max_length=999, null=True)),
                ('footer_youtube_link', models.URLField(blank=True, max_length=999, null=True)),
                ('footer_copyright', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, null=True, upload_to='homeimages')),
                ('group_link', models.URLField(blank=True, max_length=999, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageTopSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to='homeimages')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageYouGet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='address',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='email',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_contact_title',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_copyright',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_facebook_link',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_instagram_link',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_linkedin_link',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_links_title',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_payment_title',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_quotes',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_twitter_link',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='footer_youtube_link',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='group_link',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='homepagetitleandextra',
            name='phone',
        ),
        migrations.AddField(
            model_name='homepagetitleandextra',
            name='happy_client',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='homepagetitleandextra',
            name='partners',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='homepagetitleandextra',
            name='project_done',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
