# Generated by Django 4.2.1 on 2023-05-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('patient_first_name', models.CharField(max_length=50)),
                ('patient_last_name', models.CharField(max_length=50)),
                ('patient_type_blood', models.CharField(max_length=50)),
            ],
        ),
    ]