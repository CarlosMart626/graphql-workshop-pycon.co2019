# Generated by Django 2.1.5 on 2019-01-28 01:38

from django.db import migrations, models
import simplemde.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190127_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', simplemde.fields.SimpleMDEField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.RemoveField(
            model_name='invitee',
            name='id',
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default='-', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='cover_image',
            field=models.ImageField(default='-', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='invitee',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
