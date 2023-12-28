# Generated by Django 4.0 on 2022-01-09 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('store', '0017_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Mã giảm giá')),
                ('is_active', models.BooleanField(default=True, verbose_name='Còn sử dụng được không')),
                ('type', models.IntegerField(verbose_name='Thể loại - 0 là trừ tiền hàng, 1 là freeship')),
                ('discount', models.FloatField(default=0, verbose_name='Giảm giá - số là trừ tiền,dạng thập phân là giảm %')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(verbose_name='Thời gian đặt'),
        ),
        migrations.CreateModel(
            name='UserVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.voucher')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian đặt')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tổng tiền')),
                ('order', models.ManyToManyField(to='store.Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
