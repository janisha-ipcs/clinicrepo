# Generated by Django 4.2.7 on 2023-12-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='name', null=True)),
                ('email', models.TextField(db_column='email', null=True)),
                ('msg', models.TextField(db_column='msg', null=True)),
            ],
        ),
    ]
