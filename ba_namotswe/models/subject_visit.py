from datetime import date
from django.db import models
from django.core.validators import MinValueValidator

from simple_history.models import HistoricalRecords

from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_base.model.validators.date import date_not_future
from edc_consent.model_mixins import RequiresConsentMixin
from edc_constants.constants import ON_STUDY, YES
from edc_metadata.model_mixins import CreatesMetadataModelMixin
from edc_visit_tracking.constants import SCHEDULED, CHART
from edc_visit_tracking.model_mixins import VisitModelMixin

from .appointment import Appointment


class SubjectVisit(VisitModelMixin, CreatesMetadataModelMixin, RequiresConsentMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

    visit_date = models.DateField(
        verbose_name="Visit Date",
        validators=[
            MinValueValidator(date(2001, 1, 1)),
            date_not_future])

    objects = models.Manager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.id:
            self.study_status = ON_STUDY
            self.reason = self.reason or SCHEDULED
            self.require_crfs = YES
            self.info_source = CHART
        super(SubjectVisit, self).save(*args, **kwargs)

    class Meta(VisitModelMixin.Meta):
        app_label = 'ba_namotswe'
        consent_model = 'ba_namotswe.subjectconsent'
        unique_together = (
            ('subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_code'),
            ('subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_date'),
        )
        ordering = (('subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_code', 'visit_date', ))
