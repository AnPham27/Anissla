# Generated by Django 4.1.7 on 2023-04-04 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_tops_accessory_rename_bottoms_bottom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('shoe', 'Shoe'), ('accessory', 'Accessory')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='top',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
    ]
