# Generated by Django 3.1.4 on 2020-12-09 14:22

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
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ledger', models.CharField(choices=[('TRAVEL', 'TRAVEL'), ('RENT', 'RENT'), ('INTERNET', 'INTERNET'), ('AIRTIME', 'AIRTIME'), ('FUEL', 'FUEL'), ('MISCEllANEOUS', 'MISCEllANEOUS')], max_length=255)),
                ('reference', models.TextField()),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=255)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
