# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
        ('hallbookingapp', '0001_initial'),
        ('membershipapp', '0001_initial'),
        ('backofficeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventBannerImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_files', models.FileField(max_length=500, null=True, upload_to=b'EventFiles/banners', blank=True)),
                ('banner_type', models.IntegerField(default=0, choices=[(0, b'Event Banner'), (1, b'Sponsor Banner')])),
                ('creation_date', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_title', models.CharField(max_length=200, null=True)),
                ('event_description_indetails', models.TextField(null=True, blank=True)),
                ('to_whom_description', models.TextField(null=True, blank=True)),
                ('organised_by', models.TextField(null=True, blank=True)),
                ('event_objective', models.TextField(null=True, blank=True)),
                ('from_date', models.DateTimeField(null=True, blank=True)),
                ('to_date', models.DateTimeField(null=True, blank=True)),
                ('registration_start_date', models.DateTimeField(null=True, blank=True)),
                ('registration_end_date', models.DateTimeField(null=True, blank=True)),
                ('release_date', models.DateTimeField(null=True, blank=True)),
                ('other_location_address', models.TextField(null=True, blank=True)),
                ('member_charges', models.IntegerField(default=0, null=True, blank=True)),
                ('non_member_charges', models.IntegerField(default=0, null=True, blank=True)),
                ('other_charges_name', models.CharField(max_length=100, null=True, blank=True)),
                ('other_charges_amount', models.IntegerField(default=0, null=True, blank=True)),
                ('event_no', models.CharField(max_length=20, null=True, blank=True)),
                ('is_early_bird', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('early_member_charges', models.IntegerField(default=0, null=True, blank=True)),
                ('early_non_member_charges', models.IntegerField(default=0, null=True, blank=True)),
                ('early_bird_date', models.DateTimeField(null=True, blank=True)),
                ('discount_1', models.CharField(max_length=50, null=True, blank=True)),
                ('discount_2', models.CharField(max_length=50, null=True, blank=True)),
                ('discount_3', models.CharField(max_length=50, null=True, blank=True)),
                ('expected_members', models.IntegerField(default=0, null=True, blank=True)),
                ('expected_nonmembers', models.IntegerField(default=0, null=True, blank=True)),
                ('expected_freemembers', models.IntegerField(default=0, null=True, blank=True)),
                ('expected_sponsored_members', models.IntegerField(default=0, null=True, blank=True)),
                ('expected_capacity', models.IntegerField(default=0, null=True, blank=True)),
                ('priority', models.IntegerField(default=0, choices=[(0, b'No Priority'), (1, b'Priority 1'), (2, b'Priority 2'), (3, b'Priority 3')])),
                ('event_mode', models.IntegerField(default=0, choices=[(0, b'Open To All'), (1, b'On Payment'), (2, b'By Invitation')])),
                ('online_payment', models.IntegerField(default=0, choices=[(0, b'OFF'), (1, b'ON')])),
                ('meta_title', models.TextField(null=True, blank=True)),
                ('meta_keyword', models.TextField(null=True, blank=True)),
                ('meta_description', models.TextField(null=True, blank=True)),
                ('meta_keyphrases', models.TextField(null=True, blank=True)),
                ('event_status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive'), (2, b'Deleted')])),
                ('view_status', models.IntegerField(default=0, choices=[(0, b'OFF'), (1, b'ON')])),
                ('current_event_stat', models.IntegerField(default=0, choices=[(0, b'OK'), (1, b'CANCEL'), (2, b'POSTPONE')])),
                ('created_by', models.CharField(max_length=80, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('contact_person1', models.ForeignKey(related_name='contact_person1', blank=True, to='backofficeapp.SystemUserProfile', null=True)),
                ('contact_person2', models.ForeignKey(related_name='contact_person2', blank=True, to='backofficeapp.SystemUserProfile', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipantReportTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_no', models.CharField(max_length=100, null=True, blank=True)),
                ('name_of_organisation', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('contact_person_name', models.CharField(max_length=100, null=True)),
                ('contact_person_number', models.CharField(max_length=50, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('contact_person_email_id', models.CharField(max_length=100, null=True)),
                ('is_member', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('created_by', models.CharField(max_length=80, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipantUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_user_name', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('contact_no', models.CharField(max_length=50, null=True)),
                ('email_id', models.CharField(max_length=100, null=True)),
                ('created_by', models.CharField(max_length=80, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('is_invitee', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_attendees', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_active', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('register_status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive'), (2, b'Deleted')])),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_no', models.CharField(max_length=100, null=True, blank=True)),
                ('name_of_organisation', models.CharField(max_length=100, null=True)),
                ('enroll_type', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'Company'), (b'IN', b'Individual')])),
                ('address', models.TextField(null=True, blank=True)),
                ('contact_person_name', models.CharField(max_length=100, null=True)),
                ('contact_person_number', models.CharField(max_length=50, null=True)),
                ('contact_person_number_two', models.CharField(max_length=50, null=True)),
                ('office_contact', models.CharField(max_length=50, null=True)),
                ('contact_person_email_id', models.CharField(max_length=100, null=True)),
                ('no_of_participant', models.IntegerField(default=1, null=True)),
                ('total_amount', models.FloatField(default=0, null=True, blank=True)),
                ('total_fees_amount', models.FloatField(default=0, null=True, blank=True)),
                ('extra_gst_amount', models.FloatField(default=0, null=True, blank=True)),
                ('total_discount_amount', models.FloatField(default=0, null=True, blank=True)),
                ('payment_mode', models.CharField(default=b'Online', max_length=100, choices=[(b'Online', b'Online'), (b'Offline', b'Offline')])),
                ('payment_method', models.IntegerField(blank=True, null=True, choices=[(0, b'Cash'), (1, b'Cheque'), (2, b'NEFT')])),
                ('payment_status', models.IntegerField(default=0, choices=[(0, b'Pending'), (1, b'Inprogress'), (2, b'Initiated'), (3, b'Failed'), (4, b'Paid')])),
                ('cash_receipt_no', models.CharField(max_length=50, null=True, blank=True)),
                ('cheque_no', models.CharField(max_length=10, null=True, blank=True)),
                ('bank_name', models.CharField(max_length=100, null=True)),
                ('cheque_date', models.DateField(null=True)),
                ('trasanction_id', models.CharField(max_length=50, null=True, blank=True)),
                ('tds_amount', models.FloatField(default=0, null=True, blank=True)),
                ('register_status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive'), (2, b'Deleted')])),
                ('gst', models.CharField(max_length=50, null=True, blank=True)),
                ('gst_in', models.CharField(default=b'NA', max_length=2, choices=[(b'UP', b'Under Process'), (b'AP', b'Applicable'), (b'NA', b'Not Applicable')])),
                ('pan', models.CharField(max_length=12, null=True, blank=True)),
                ('is_member', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_other', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_invitee', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_attendees', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('medium_source', models.IntegerField(default=0, choices=[(0, b'Email from MCCIA'), (1, b'Website'), (2, b'Social Media'), (3, b'Referred by Other')])),
                ('social_medium_source', models.IntegerField(default=0, choices=[(0, b'Facebook'), (1, b'LinkedIn'), (2, b'WhatsApp')])),
                ('created_by', models.CharField(max_length=80, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_active', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('companydetail', models.ForeignKey(blank=True, to='membershipapp.CompanyDetail', null=True)),
                ('event', models.ForeignKey(blank=True, to='eventsapp.EventDetails', null=True)),
                ('nonmemberdetail', models.ForeignKey(blank=True, to='membershipapp.NonMemberDetail', null=True)),
                ('user_details', models.ForeignKey(blank=True, to='membershipapp.UserDetail', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventSpecialAnnouncement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('announcement', models.CharField(max_length=500, null=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(max_length=80, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('status', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
            ],
        ),
        migrations.CreateModel(
            name='EventSponsorImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_files', models.FileField(max_length=500, null=True, upload_to=b'EventFiles/banners', blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('creation_date', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(max_length=500, null=True, blank=True)),
                ('event_id', models.ForeignKey(blank=True, to='eventsapp.EventDetails', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_type', models.CharField(max_length=150, blank=True)),
                ('created_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
            ],
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promo_code', models.CharField(max_length=150, null=True, blank=True)),
                ('for_whom', models.CharField(max_length=250, null=True, blank=True)),
                ('percent_discount', models.CharField(max_length=50, null=True, blank=True)),
                ('discounted_amount', models.IntegerField(default=0, null=True, blank=True)),
                ('created_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('event_details', models.ForeignKey(blank=True, to='eventsapp.EventDetails', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='eventparticipantuser',
            name='event_user',
            field=models.ForeignKey(blank=True, to='eventsapp.EventRegistration', null=True),
        ),
        migrations.AddField(
            model_name='eventparticipantreporttable',
            name='event_registration',
            field=models.ForeignKey(blank=True, to='eventsapp.EventRegistration', null=True),
        ),
        migrations.AddField(
            model_name='eventdetails',
            name='event_type',
            field=models.ForeignKey(blank=True, to='eventsapp.EventType', null=True),
        ),
        migrations.AddField(
            model_name='eventdetails',
            name='hall_details',
            field=models.ForeignKey(blank=True, to='hallbookingapp.HallDetail', null=True),
        ),
        migrations.AddField(
            model_name='eventdetails',
            name='organising_committee',
            field=models.ForeignKey(blank=True, to='adminapp.Committee', null=True),
        ),
        migrations.AddField(
            model_name='eventbannerimage',
            name='event_detail_id',
            field=models.ForeignKey(blank=True, to='eventsapp.EventDetails', null=True),
        ),
    ]
