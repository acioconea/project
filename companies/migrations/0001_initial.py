# Generated by Django 4.2.7 on 2023-11-21 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aplicatie1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=50)),
                ('company_type', models.CharField(choices=[('SRL', 'S.R.L.'), ('SA', 'S.A.')], max_length=5)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicatie1.location')),
            ],
        ),
    ]
