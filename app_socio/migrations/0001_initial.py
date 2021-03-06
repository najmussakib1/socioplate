# Generated by Django 3.2.5 on 2021-09-10 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='userpost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('likes', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('lovers', models.ManyToManyField(related_name='lovers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
