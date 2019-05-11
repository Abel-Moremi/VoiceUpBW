# Generated by Django 2.1.7 on 2019-05-10 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voiceUpPost', '0003_auto_20190510_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='voiceUpPost.VoiceUpPost')),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
