# Generated by Django 5.1.2 on 2024-10-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('cover', models.CharField(choices=[('HARD', 'Hard'), ('SOFT', 'Soft')], max_length=4)),
                ('inventory', models.PositiveIntegerField()),
                ('daily_fee', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
