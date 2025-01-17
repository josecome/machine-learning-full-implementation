# Generated by Django 4.1 on 2024-11-25 15:17

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
            name='Person',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('created_date', models.DateField(null=True)),
                ('updated_date', models.DateField(null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sepal_length', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sepal_width', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('petal_length', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('petal_width', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sel_variety', models.CharField(max_length=20, null=True)),
                ('pred_variety', models.CharField(max_length=20, null=True)),
                ('date_created', models.DateField(null=True)),
                ('date_updated', models.DateField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'db_table': 'preferences',
            },
        ),
    ]
