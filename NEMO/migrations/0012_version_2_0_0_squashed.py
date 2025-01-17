# Generated by Django 2.2.27 on 2022-03-17 13:16

import django.db.models.deletion
from django.db import migrations, models

import NEMO.utilities


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# NEMO.migrations.0014_version_2_2_0

class Migration(migrations.Migration):

    replaces = [('NEMO', '0012_version_2_0_0'), ('NEMO', '0013_version_2_1_0'), ('NEMO', '0014_version_2_2_0'), ('NEMO', '0015_area_maximum_capacity'), ('NEMO', '0016_area_reservation_warning'), ('NEMO', '0017_remove_facility_and_site_names_from_help_text'), ('NEMO', '0018_area_count_staff_in_occupancy'), ('NEMO', '0019_user_type_not_required')]

    dependencies = [
        ('NEMO', '0011_version_1_22_0'),
    ]

    def create_proxr_interlock_card_category(apps, schema_editor):
        InterlockCardCategory = apps.get_model("NEMO", "InterlockCardCategory")
        if not InterlockCardCategory.objects.filter(key="proxr").exists():
            proxr_category = InterlockCardCategory.objects.create(name="ProXr", key="proxr")
            proxr_category.save()

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='_post_usage_questions',
            field=models.TextField(blank=True, db_column='post_usage_questions', help_text='Upon logging off a tool, questions can be asked such as how much consumables were used by the user. This field will only accept JSON format', null=True),
        ),
        migrations.AddField(
            model_name='interlockcard',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='_description',
            field=models.TextField(blank=True, db_column='description', help_text='HTML syntax could be used', null=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='_serial',
            field=models.CharField(blank=True, db_column='serial', help_text='Serial Number', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='_image',
            field=models.ImageField(blank=True, db_column='image', help_text='An image that represent the tool. Maximum width and height are 500px', upload_to=NEMO.utilities.get_tool_image_filename),
        ),
        migrations.AddField(
            model_name='physicalaccesslevel',
            name='allow_staff_access',
            field=models.BooleanField(default=False, help_text='Check this box to allow access to Staff users without explicitly granting them access'),
        ),
        migrations.CreateModel(
            name='AlertCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Alert categories',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='alert',
            name='category',
            field=models.CharField(blank=True, help_text='A category/type for this alert.', max_length=200),
        ),
        migrations.AddField(
            model_name='alert',
            name='deleted',
            field=models.BooleanField(default=False, help_text="Indicates the alert has been deleted and won't be shown anymore"),
        ),
        migrations.AddField(
            model_name='alert',
            name='expired',
            field=models.BooleanField(default=False, help_text="Indicates the alert has expired and won't be shown anymore"),
        ),
        migrations.AddField(
            model_name='comment',
            name='staff_only',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(
            code=create_proxr_interlock_card_category,
        ),
        migrations.AddField(
            model_name='area',
            name='maximum_capacity',
            field=models.PositiveIntegerField(default=0, help_text='The maximum number of people allowed in this area at any given time. Set to 0 for unlimited.'),
        ),
        migrations.AddField(
            model_name='area',
            name='reservation_warning',
            field=models.PositiveIntegerField(blank=True, help_text='The number of simultaneous users (with at least one reservation in this area) allowed before a warning is displayed when creating a reservation.', null=True),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='exclude_from_configuration_agenda',
            field=models.BooleanField(default=False, help_text='Reservations containing this configuration will be excluded from the Configuration Agenda page.'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='self_configuration',
            field=models.BooleanField(default=False, help_text='When checked, indicates that the user will perform their own tool configuration (instead of requesting that the staff configure it for them).'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='short_notice',
            field=models.BooleanField(default=None, help_text='Indicates that the reservation was made after the configuration deadline for a tool. Staff may not have enough time to properly configure the tool before the user is scheduled to use it.'),
        ),
        migrations.AlterField(
            model_name='task',
            name='safety_hazard',
            field=models.BooleanField(default=None, help_text='Indicates that this task represents a safety hazard.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='badge_number',
            field=models.PositiveIntegerField(blank=True, help_text='The badge number associated with this user. This number must correctly correspond to a user in order for the tablet-login system (in the lobby) to work properly.', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='landingpagechoice',
            name='secure_referral',
            field=models.BooleanField(default=True, help_text="Improves security by blocking HTTP referer [sic] information from the targeted page. Enabling this prevents the target page from manipulating the calling page's DOM with JavaScript. This should always be used for external links. It is safe to uncheck this when linking within the site. Leave this box checked if you don't know what this means"),
        ),
        migrations.AlterField(
            model_name='landingpagechoice',
            name='url',
            field=models.CharField(help_text='The URL that the choice leads to when clicked. Relative paths such as /calendar/ are used when linking within the site. Use fully qualified URL paths such as https://www.google.com/ to link to external sites.', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user can log in. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='area',
            name='count_staff_in_occupancy',
            field=models.BooleanField(default=True, help_text='Indicates that staff users will count towards maximum capacity.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NEMO.UserType'),
        ),
    ]
