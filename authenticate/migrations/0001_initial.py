# Generated by Django 4.1.3 on 2023-03-05 14:14

import authenticate.managers
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('lname', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=70, null=True)),
                ('institute', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('object', authenticate.managers.UserManager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('Auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('posting_time', models.DateTimeField(auto_now_add=True)),
                ('is_sold', models.BooleanField(blank=True, default=False, null=True)),
                ('Auction_expiry', models.DateTimeField()),
                ('highest_bid', models.CharField(max_length=256)),
                ('final_bidder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellingItem',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=256)),
                ('item_description', models.TextField()),
                ('item_posted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_sold', models.BooleanField(blank=True, default=False, null=True)),
                ('item_category', models.CharField(blank=True, max_length=256, null=True)),
                ('is_auction_item', models.BooleanField(blank=True, default=False, null=True)),
                ('item_location', models.TextField(blank=True, null=True)),
                ('item_price', models.TextField(blank=True, null=True)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.sellingitem')),
                ('wishlist_owner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_holder_name', models.TextField(null=True)),
                ('card_number', models.TextField(max_length=16, null=True)),
                ('expiry', models.DateField(null=True)),
                ('owner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_status', models.BooleanField(blank=True, default=False, null=True)),
                ('address', models.TextField(default='some building')),
                ('payment_method', models.TextField(default='some payment')),
                ('card_info', models.TextField(default='some card info')),
                ('price', models.TextField(blank=True, default='100', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('buyer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item_for_sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.sellingitem')),
                ('seller_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image')),
                ('item_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.sellingitem')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('bid_id', models.AutoField(primary_key=True, serialize=False)),
                ('bid_price', models.CharField(blank=True, max_length=256, null=True)),
                ('Auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.auction')),
                ('bidder_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.sellingitem'),
        ),
        migrations.AddField(
            model_name='auction',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=200)),
                ('address3', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
