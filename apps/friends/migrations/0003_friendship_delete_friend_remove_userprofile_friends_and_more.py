# Generated by Django 4.2.1 on 2023-05-08 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_friendrequest_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(choices=[('OUTGOING_REQUEST', 'Outgoing Request'), ('INCOMING_REQUEST', 'Incoming Request'), ('ALREADY_FRIENDS', 'Already Friends')], max_length=32),
        ),
        migrations.AddField(
            model_name='friendship',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='friends.userprofile'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friends.userprofile'),
        ),
    ]