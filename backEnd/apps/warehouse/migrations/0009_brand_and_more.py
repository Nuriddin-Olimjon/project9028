# Generated by Django 4.0.4 on 2023-01-22 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_remove_returnedinvoice_is_deleted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='current_price',
            new_name='current_arrival_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='shelf_life',
        ),
        migrations.AddField(
            model_name='product',
            name='current_selling_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='warehouse.brand'),
            preserve_default=False,
        ),
    ]
