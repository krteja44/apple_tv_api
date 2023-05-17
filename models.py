from django.db import models
from django.utils.timezone import now
import uuid


class AiringDataGui(models.Model):
    network_id = models.BigIntegerField(blank=True, null=True)
    airing_id = models.BigIntegerField(blank=True, null=True)
    airing_external_id = models.CharField(blank=True, default='', max_length=40)
    airing_name = models.CharField(blank=True, default='', max_length=40)
    airing_duration_sec = models.BigIntegerField(blank=True, null=True)
    airing_start_time = models.DateTimeField(max_length=100, null=True)
    airing_end_time = models.DateTimeField(max_length=100, null=True)
    airing_status = models.CharField(blank=True, default='', max_length=40)
    airing_source = models.CharField(blank=True, default='', max_length=40)

    class Meta:
        managed = False
        db_table = "raw_airing_data_gui"


class AiringInfo(models.Model):
    airing_duration_sec = models.BigIntegerField(blank=True, null=True)
    airing_end_time = models.DateTimeField(max_length=100, null=True)
    airing_external_id = models.CharField(blank=True, default='', max_length=40)
    airing_id = models.BigIntegerField(blank=True, null=True)
    airing_name = models.CharField(blank=True, default='', max_length=40)
    airing_source = models.CharField(blank=True, default='', max_length=40)
    airing_start_time = models.DateTimeField(max_length=100, null=True)
    network_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "apple_runs_mapping"


class RunsInfo(models.Model):
    run_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, max_length=36)
    created = models.DateTimeField(default=now, editable=False)
    data_validation_status = models.CharField(blank=True, default='', max_length=40)
    scheduler_status = models.CharField(blank=True, default='', max_length=40)
    run_desc = models.TextField(blank=True, default='')
    placement_run_type = models.BigIntegerField(default=1)

    class Meta:
        managed = False
        db_table = "apple_runs"


class AuthUser(models.Model):
    username = models.CharField(blank=False, default='', max_length=150)
    password = models.CharField(blank=False, default='', max_length=40)
    email = models.EmailField(blank=False, default='', max_length=254)
    first_name = models.CharField(blank=True, default='', max_length=40)
    last_name = models.CharField(blank=True, default='', max_length=40)
    date_joined = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    user_type = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthHistory(models.Model):
    username = models.CharField(blank=False, default='', max_length=150)
    password = models.CharField(blank=False, default='', max_length=40)
    email = models.EmailField(blank=False, default='', max_length=254)
    pattern_match = models.CharField(blank=False, default='', max_length=40)

    class Meta:
        managed = True
        db_table = "user_auth_history"
