# Generated by Django 4.2.3 on 2023-07-26 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TJ', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='img_url',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='journals', to='TJ.user')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('writeup', models.TextField()),
                ('photo_album', models.ImageField(upload_to='')),
                ('journal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='TJ.journal')),
            ],
        ),
    ]