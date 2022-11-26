# Generated by Django 4.0 on 2022-01-09 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_parque_senha_senha_parque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senha',
            name='parque',
        ),
        migrations.AddField(
            model_name='parque',
            name='senha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Parque', to='login.senha'),
        ),
    ]