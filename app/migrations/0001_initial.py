# Generated by Django 4.1.7 on 2023-05-30 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField()),
                ('product_name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField(auto_now=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pros', to='app.productcategory')),
            ],
        ),
    ]
