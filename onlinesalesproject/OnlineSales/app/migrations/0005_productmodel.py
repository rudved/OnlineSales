# Generated by Django 2.2.5 on 2019-11-11 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_loginmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('p_no', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=30)),
                ('p_price', models.FloatField()),
                ('p_quantity', models.IntegerField()),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.MarchentModel')),
            ],
        ),
    ]
