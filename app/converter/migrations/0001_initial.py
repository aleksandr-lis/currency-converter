# Generated by Django 2.2.6 on 2019-10-21 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('code', models.CharField(editable=False, max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_base', to='converter.Currencies')),
                ('curr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_curr', to='converter.Currencies')),
            ],
        ),
    ]
