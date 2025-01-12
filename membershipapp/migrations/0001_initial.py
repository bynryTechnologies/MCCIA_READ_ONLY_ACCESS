# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('adminapp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100, null=True, blank=True)),
                ('description_of_business', models.CharField(max_length=200, null=True, blank=True)),
                ('establish_year', models.IntegerField(null=True, blank=True)),
                ('company_scale', models.CharField(default=b'MR', max_length=2, choices=[(b'MR', b'Micro'), (b'SM', b'Small'), (b'MD', b'Medium'), (b'LR', b'Large')])),
                ('block_inv_plant', models.CharField(max_length=50, null=True, blank=True)),
                ('block_inv_land', models.CharField(max_length=50, null=True, blank=True)),
                ('block_inv_total', models.CharField(max_length=50, null=True, blank=True)),
                ('textexport', models.TextField(null=True, blank=True)),
                ('textimport', models.TextField(null=True, blank=True)),
                ('rnd_facility', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('govt_recognised', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('iso', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('iso_detail', models.TextField(null=True, blank=True)),
                ('foreign_collaboration', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('eou', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('eou_detail', models.CharField(max_length=100, null=True, blank=True)),
                ('total_manager', models.IntegerField(default=0, null=True, blank=True)),
                ('total_staff', models.IntegerField(default=0, null=True, blank=True)),
                ('total_workers', models.IntegerField(default=0, null=True, blank=True)),
                ('total_employees', models.IntegerField(default=0, null=True, blank=True)),
                ('industrydescription_other', models.CharField(max_length=100, null=True, blank=True)),
                ('same_as_above', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('ceo_email_confirmation', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('turnover_range', models.IntegerField(blank=True, null=True, choices=[(0, b'0-1'), (1, b'1-5'), (2, b'5-25'), (3, b'25-100'), (4, b'100-500'), (5, b'500+')])),
                ('employee_range', models.IntegerField(blank=True, null=True, choices=[(0, b'0-10'), (1, b'10-100'), (2, b'100-500'), (3, b'500-1000'), (4, b'1000+')])),
                ('is_member', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('member_event_email', models.TextField(null=True, blank=True)),
                ('gst', models.CharField(max_length=20, null=True, blank=True)),
                ('enroll_type', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'Company'), (b'IN', b'Individual')])),
                ('created_by', models.CharField(max_length=100, null=True, blank=True)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('exportcountry', models.ManyToManyField(related_name='export_country', to='adminapp.Country', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HOD_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hr_name', models.CharField(max_length=50, null=True, blank=True)),
                ('hr_contact', models.CharField(max_length=50, null=True, blank=True)),
                ('hr_email', models.CharField(max_length=80, null=True, blank=True)),
                ('finance_name', models.CharField(max_length=50, null=True, blank=True)),
                ('finance_contact', models.CharField(max_length=50, null=True, blank=True)),
                ('finance_email', models.CharField(max_length=80, null=True, blank=True)),
                ('marketing_name', models.CharField(max_length=50, null=True, blank=True)),
                ('marketing_contact', models.CharField(max_length=50, null=True, blank=True)),
                ('marketing_email', models.CharField(max_length=80, null=True, blank=True)),
                ('IT_name', models.CharField(max_length=50, null=True, blank=True)),
                ('IT_contact', models.CharField(max_length=50, null=True, blank=True)),
                ('IT_email', models.CharField(max_length=80, null=True, blank=True)),
                ('corp_rel_name', models.CharField(max_length=50, null=True, blank=True)),
                ('corp_rel_contact', models.CharField(max_length=50, null=True, blank=True)),
                ('corp_rel_email', models.CharField(max_length=80, null=True, blank=True)),
                ('tech_name', models.CharField(max_length=80, null=True, blank=True)),
                ('tech_contact', models.CharField(max_length=80, null=True, blank=True)),
                ('tech_email', models.CharField(max_length=80, null=True, blank=True)),
                ('rnd_name', models.CharField(max_length=80, null=True, blank=True)),
                ('rnd_contact', models.CharField(max_length=80, null=True, blank=True)),
                ('rnd_email', models.CharField(max_length=80, null=True, blank=True)),
                ('exim_name', models.CharField(max_length=80, null=True, blank=True)),
                ('exim_contact', models.CharField(max_length=80, null=True, blank=True)),
                ('exim_email', models.CharField(max_length=80, null=True, blank=True)),
                ('stores_name', models.CharField(max_length=80, null=True, blank=True)),
                ('stores_contact', models.CharField(max_length=80, null=True, blank=True)),
                ('stores_email', models.CharField(max_length=80, null=True, blank=True)),
                ('purchase_name', models.CharField(max_length=80, null=True, blank=True)),
                ('purchase_contact', models.CharField(max_length=80, null=True, blank=True)),
                ('purchase_email', models.CharField(max_length=80, null=True, blank=True)),
                ('production_name', models.CharField(max_length=80, null=True, blank=True)),
                ('production_contact', models.CharField(max_length=80, null=True, blank=True)),
                ('production_email', models.CharField(max_length=80, null=True, blank=True)),
                ('quality_name', models.CharField(max_length=80, null=True, blank=True)),
                ('quality_contact', models.CharField(max_length=80, null=True, blank=True)),
                ('quality_email', models.CharField(max_length=80, null=True, blank=True)),
                ('supply_chain_name', models.CharField(max_length=80, null=True, blank=True)),
                ('supply_chain_contact', models.CharField(max_length=80, null=True, blank=True)),
                ('supply_chain_email', models.CharField(max_length=80, null=True, blank=True)),
                ('created_by', models.CharField(max_length=100, blank=True)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
            ],
        ),
        migrations.CreateModel(
            name='MembershipInvoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valid_invalid_member', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('subscription_charges', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('entrance_fees', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('tax', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('amount_payable', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('without_adv_amount_payable', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('financial_year', models.CharField(max_length=30, null=True, blank=True)),
                ('last_due_amount', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('last_advance_amount', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('invoice_for', models.CharField(default=b'NEW', max_length=12, null=True, blank=True, choices=[(b'NEW', b'NEW'), (b'RENEW', b'RENEW'), (b'RE-ASSOCIATE', b'RE-ASSOCIATE')])),
                ('is_paid', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_settled', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('settle_amount', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('is_tds', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('tds_amount', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('turnover_range', models.IntegerField(blank=True, null=True, choices=[(0, b'0-1'), (1, b'1-5'), (2, b'5-25'), (3, b'25-100'), (4, b'100-500'), (5, b'500+')])),
                ('employee_range', models.IntegerField(blank=True, null=True, choices=[(0, b'0-10'), (1, b'10-100'), (2, b'100-500'), (3, b'500-1000'), (4, b'1000+')])),
                ('user_type', models.CharField(blank=True, max_length=20, null=True, choices=[(b'Member', b'Member'), (b'Associate', b'Associate'), (b'Life Membership', b'Life Membership'), (b'I', b'I')])),
                ('membership_acceptance_date', models.DateField(null=True, blank=True)),
                ('created_by', models.CharField(max_length=70, null=True, blank=True)),
                ('updated_by', models.CharField(max_length=70, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('membership_category', models.ForeignKey(blank=True, to='adminapp.MembershipCategory', null=True)),
                ('membership_slab', models.ForeignKey(blank=True, to='adminapp.MembershipSlab', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipTypeTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_company_name', models.CharField(max_length=100, null=True, blank=True)),
                ('old_user_type', models.CharField(blank=True, max_length=20, null=True, choices=[(b'Member', b'Member'), (b'Associate', b'Associate'), (b'Life Membership', b'Life Membership'), (b'I', b'I')])),
                ('old_enroll_type', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'Company'), (b'IN', b'Individual')])),
                ('old_member_associate_no', models.CharField(default=None, max_length=150, null=True, blank=True)),
                ('old_acceptance_date', models.DateField(null=True, blank=True)),
                ('last_membership_year', models.CharField(max_length=100, null=True, blank=True)),
                ('last_renewal_year', models.CharField(max_length=30, null=True, blank=True)),
                ('last_renewal_status', models.CharField(default=b'NOT_STARTED', max_length=15, null=True, blank=True, choices=[(b'NOT_STARTED', b'NOT_STARTED'), (b'STARTED', b'STARTED'), (b'COMPLETED', b'COMPLETED')])),
                ('new_user_type', models.CharField(blank=True, max_length=20, null=True, choices=[(b'Member', b'Member'), (b'Associate', b'Associate'), (b'Life Membership', b'Life Membership'), (b'I', b'I')])),
                ('new_member_associate_no', models.CharField(default=None, max_length=150, null=True, blank=True)),
                ('new_acceptance_date', models.DateField(null=True, blank=True)),
                ('created_by', models.CharField(max_length=70, blank=True)),
                ('updated_by', models.CharField(max_length=70, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('old_category', models.ForeignKey(blank=True, to='adminapp.MembershipCategory', null=True)),
                ('old_slab', models.ForeignKey(blank=True, to='adminapp.MembershipSlab', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('created_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('updated_by', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NonMemberDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('gst', models.CharField(max_length=20, null=True, blank=True)),
                ('enroll_type', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'Company'), (b'IN', b'Individual')])),
                ('email', models.CharField(max_length=80, null=True, blank=True)),
                ('extra_email', models.TextField(null=True, blank=True)),
                ('created_by', models.CharField(max_length=70, blank=True)),
                ('updated_by', models.CharField(max_length=70, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True, choices=[(True, True), (False, False)])),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('company', models.ForeignKey(blank=True, to='membershipapp.CompanyDetail', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_payable', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('amount_paid', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('partial_amount_paid', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('amount_due', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('amount_last_advance', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('amount_next_advance', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('next_advance_gst_amount', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('cheque_no', models.CharField(max_length=100, null=True, blank=True)),
                ('cheque_date', models.DateField(null=True, blank=True)),
                ('bank_name', models.CharField(max_length=150, null=True, blank=True)),
                ('neft_transfer_id', models.CharField(max_length=150, null=True, blank=True)),
                ('cash_amount', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('cheque_bounce_charge', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('receipt_no', models.CharField(max_length=100, null=True, blank=True)),
                ('receipt_date', models.DateField(null=True, blank=True)),
                ('user_Payment_Type', models.CharField(default=b'Cheque', max_length=20, null=True, blank=True, choices=[(b'Cheque', b'Cheque'), (b'Cash', b'Cash'), (b'NEFT', b'NEFT'), (b'Online', b'Online')])),
                ('payment_date', models.DateField(null=True, blank=True)),
                ('payment_received_status', models.CharField(default=b'UnPaid', max_length=20, null=True, blank=True, choices=[(b'Paid', b'Paid'), (b'UnPaid', b'UnPaid'), (b'Partial', b'Partial'), (b'Advance', b'Advance')])),
                ('financial_year', models.CharField(max_length=100, null=True, blank=True)),
                ('bk_no', models.CharField(max_length=20, null=True, blank=True)),
                ('is_cheque_bounce', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_neft_failed', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_other', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_amount_refund', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_settled', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('settle_amount', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('is_tds', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('tds_amount', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('payment_remark', models.CharField(max_length=50, null=True, blank=True)),
                ('created_by', models.CharField(max_length=100, null=True, blank=True)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('membershipInvoice', models.ForeignKey(blank=True, to='membershipapp.MembershipInvoice', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RenewLetterSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row_type', models.IntegerField(default=0, choices=[(0, b'Manual Letter'), (1, b'Schedule'), (2, b'Automate Letter'), (3, b'Membership Schedule')])),
                ('renew_letter', models.TextField(null=True, blank=True)),
                ('renew_schedule', models.FileField(null=True, upload_to=b'Renewal_Schedule', blank=True)),
                ('renew_membership_schedule', models.FileField(null=True, upload_to=b'Renewal_Schedule', blank=True)),
                ('created_by', models.CharField(max_length=80, null=True, blank=True)),
                ('updated_by', models.CharField(max_length=80, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
            ],
        ),
        migrations.CreateModel(
            name='Top3Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.CharField(max_length=100, blank=True)),
                ('name', models.EmailField(max_length=80, blank=True)),
                ('created_by', models.CharField(max_length=100, blank=True)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ceo_name', models.CharField(max_length=100, null=True, blank=True)),
                ('ceo_email', models.EmailField(max_length=80, null=True, blank=True)),
                ('ceo_designation', models.CharField(max_length=50, null=True, blank=True)),
                ('ceo_cellno', models.CharField(max_length=50, null=True, blank=True)),
                ('person_name', models.CharField(max_length=50, null=True, blank=True)),
                ('person_email', models.CharField(max_length=50, null=True, blank=True)),
                ('person_designation', models.CharField(max_length=50, null=True, blank=True)),
                ('person_cellno', models.CharField(max_length=50, null=True, blank=True)),
                ('correspond_address', models.TextField(null=True, blank=True)),
                ('correspond_cellno', models.CharField(max_length=50, null=True, blank=True)),
                ('correspond_email', models.CharField(max_length=80, null=True, blank=True)),
                ('correspond_pincode', models.CharField(max_length=8, null=True, blank=True)),
                ('correspond_std1', models.CharField(max_length=100, null=True, blank=True)),
                ('correspond_std2', models.CharField(max_length=100, null=True, blank=True)),
                ('correspond_landline1', models.CharField(max_length=100, null=True, blank=True)),
                ('correspond_landline2', models.CharField(max_length=100, null=True, blank=True)),
                ('poc_name', models.CharField(max_length=100, null=True, blank=True)),
                ('poc_contact', models.CharField(max_length=50, null=True, blank=True)),
                ('poc_email', models.EmailField(max_length=80, null=True, blank=True)),
                ('factory_cellno', models.CharField(max_length=50, null=True, blank=True)),
                ('factory_address', models.CharField(max_length=200, null=True, blank=True)),
                ('factory_pincode', models.CharField(max_length=8, null=True, blank=True)),
                ('factory_std1', models.CharField(max_length=10, null=True, blank=True)),
                ('factory_std2', models.CharField(max_length=10, null=True, blank=True)),
                ('factory_landline1', models.CharField(max_length=100, null=True, blank=True)),
                ('factory_landline2', models.CharField(max_length=100, null=True, blank=True)),
                ('website', models.CharField(max_length=100, null=True, blank=True)),
                ('gst', models.CharField(max_length=50, null=True, blank=True)),
                ('gst_in', models.CharField(default=b'NA', max_length=2, choices=[(b'UP', b'Under Process'), (b'AP', b'Applicable'), (b'NA', b'Not Applicable')])),
                ('pan', models.CharField(max_length=12, null=True, blank=True)),
                ('aadhar', models.CharField(max_length=16, null=True, blank=True)),
                ('awards', models.CharField(max_length=50, null=True, blank=True)),
                ('membership_type', models.CharField(default=b'MM', max_length=2, choices=[(b'NM', b'Non Member'), (b'MM', b'Member')])),
                ('enroll_type', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'Company'), (b'IN', b'Individual')])),
                ('user_type', models.CharField(blank=True, max_length=20, null=True, choices=[(b'Member', b'Member'), (b'Associate', b'Associate'), (b'Life Membership', b'Life Membership'), (b'I', b'I')])),
                ('member_associate_no', models.CharField(default=None, max_length=150, null=True, blank=True)),
                ('membership_acceptance_date', models.DateField(null=True, blank=True)),
                ('annual_turnover_year', models.CharField(max_length=150, null=True, blank=True)),
                ('annual_turnover_rupees', models.CharField(max_length=100, null=True, blank=True)),
                ('membership_year', models.CharField(max_length=100, null=True, blank=True)),
                ('renewal_year', models.CharField(max_length=30, null=True, blank=True)),
                ('renewal_status', models.CharField(default=b'NOT_STARTED', max_length=15, null=True, blank=True, choices=[(b'NOT_STARTED', b'NOT_STARTED'), (b'STARTED', b'STARTED'), (b'COMPLETED', b'COMPLETED')])),
                ('exclude_from_mailing', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('valid_invalid_member', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('executive_committee_member', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('membership_ceritificate_dispatch', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('payment_method', models.CharField(default=b'Offline Pending', max_length=20, null=True, blank=True, choices=[(b'Online Pending', b'Online Pending'), (b'Offline Pending', b'Offline Pending'), (b'Confirmed', b'Confirmed'), (b'Failed', b'Failed'), (b'Deactivate', b'Deactivate')])),
                ('created_by', models.CharField(max_length=100, blank=True)),
                ('updated_by', models.CharField(max_length=100, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('is_reassociate', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('event_email', models.TextField(null=True, blank=True)),
                ('area_of_experties', models.IntegerField(default=0, null=True, blank=True, choices=[(0, b'unknown'), (1, b'Engineer'), (2, b'CA'), (3, b'Doctors'), (4, b'Consultant'), (5, b'Marketing Professional'), (6, b'Valuers'), (7, b'Individual Finance Brokers'), (8, b'Real Estate Broker'), (9, b'Lawyers Solicitors'), (10, b'Management Consultant'), (11, b'Trainer'), (12, b'Project Consultants'), (13, b'Others')])),
                ('experties_other', models.CharField(max_length=100, null=True, blank=True)),
                ('status', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
                ('mail_date', models.DateTimeField(null=True, blank=True)),
                ('mail_sent', models.IntegerField(default=0, null=True, blank=True, choices=[(0, b'Not Sent'), (1, b'Sent'), (2, b'Failed'), (3, b'Schedule')])),
                ('company', models.ForeignKey(blank=True, to='membershipapp.CompanyDetail', null=True)),
                ('correspondcity', models.ForeignKey(related_name='correspond_city', blank=True, to='adminapp.City', null=True)),
                ('correspondstate', models.ForeignKey(related_name='correspond_state', blank=True, to='adminapp.State', null=True)),
                ('factorycity', models.ForeignKey(related_name='factory_city', blank=True, to='adminapp.City', null=True)),
                ('factorystate', models.ForeignKey(related_name='factory_state', blank=True, to='adminapp.State', null=True)),
                ('membership_category', models.ForeignKey(blank=True, to='adminapp.MembershipCategory', null=True)),
                ('membership_description', models.ManyToManyField(to='adminapp.MembershipDescription', blank=True)),
                ('membership_slab', models.ForeignKey(blank=True, to='adminapp.MembershipSlab', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='top3member',
            name='userdetail',
            field=models.ForeignKey(blank=True, to='membershipapp.UserDetail', null=True),
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='userdetail',
            field=models.ForeignKey(blank=True, to='membershipapp.UserDetail', null=True),
        ),
        migrations.AddField(
            model_name='membershipuser',
            name='userdetail',
            field=models.ForeignKey(blank=True, to='membershipapp.UserDetail', null=True),
        ),
        migrations.AddField(
            model_name='membershiptypetrack',
            name='userdetail',
            field=models.ForeignKey(blank=True, to='membershipapp.UserDetail', null=True),
        ),
        migrations.AddField(
            model_name='membershipinvoice',
            name='userdetail',
            field=models.ForeignKey(blank=True, to='membershipapp.UserDetail', null=True),
        ),
        migrations.AddField(
            model_name='companydetail',
            name='hoddetail',
            field=models.ForeignKey(blank=True, to='membershipapp.HOD_Detail', null=True),
        ),
        migrations.AddField(
            model_name='companydetail',
            name='importcountry',
            field=models.ManyToManyField(related_name='import_country', to='adminapp.Country', blank=True),
        ),
        migrations.AddField(
            model_name='companydetail',
            name='industrydescription',
            field=models.ManyToManyField(to='adminapp.IndustryDescription', blank=True),
        ),
        migrations.AddField(
            model_name='companydetail',
            name='legalstatus',
            field=models.ForeignKey(blank=True, to='adminapp.LegalStatus', null=True),
        ),
    ]
