from django.contrib import admin

from edc_base.modeladmin.mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin)
from edc_visit_tracking.admin import VisitAdminMixin

from .forms import (
    SubjectConsentForm, SubjectVisitForm, TBHistoryForm, TreatmentForm, EnrollmentForm)
from .models import (
    SubjectConsent, SubjectVisit, CollectedData, Enrollment, Oi, Abstraction, Treatment, ArtRegimen,
    Appointment, TbHistory)


class BaseModelAdmin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                     ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin, admin.ModelAdmin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        return request.GET.get('next')


@admin.register(Enrollment)
class EnrollmentAdmin(BaseModelAdmin):
    form = EnrollmentForm
    radio_fields = {
        'caregiver_relation': admin.VERTICAL,
        'gender': admin.VERTICAL,
        'weight_measured': admin.VERTICAL,
        'height_measured': admin.VERTICAL}

    list_display = ('dashboard', 'initial_visit_date', 'hiv_diagnosis_date', 'art_initiation_date', )


@admin.register(Appointment)
class AppointmentAdmin(BaseModelAdmin):
    list_filter = ('best_appt_datetime', )


@admin.register(SubjectVisit)
class SubjectVisitAdmin(VisitAdminMixin, BaseModelAdmin):

    form = SubjectVisitForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'appointment' and request.GET.get('appointment'):
            kwargs["queryset"] = Appointment.objects.filter(pk=request.GET.get('appointment', 0))
        return super(VisitAdminMixin, self).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Abstraction)
class AbstractionAdmin(BaseModelAdmin):
    list_filter = ('subject_visit', )


@admin.register(Treatment)
class TreatmentAdmin(BaseModelAdmin):
    list_filter = ('perinatal_infection', )
    form = TreatmentForm


@admin.register(Oi)
class OiAdmin(BaseModelAdmin):
    list_filter = ('oi_type', )
    radio_fields = {
        'oi_type': admin.VERTICAL}


@admin.register(ArtRegimen)
class ARTRegimenAdmin(BaseModelAdmin):
    list_filter = ('name', )


@admin.register(CollectedData)
class CollectedDataAdmin(BaseModelAdmin):
    list_filter = ('arv_changes', 'tb_diagnosis', )
    radio_fields = {
        'arv_changes': admin.VERTICAL,
        'tb_diagnosis': admin.VERTICAL,
        'oi_diagnosis': admin.VERTICAL,
        'preg_diagnosis': admin.VERTICAL,
        'counselling_adhere': admin.VERTICAL,
        'transfer': admin.VERTICAL,
        'death': admin.VERTICAL}


@admin.register(TbHistory)
class TBHistoryAdmin(BaseModelAdmin):
    form = TBHistoryForm
    radio_fields = {
        'tb_type': admin.VERTICAL,
        'tb_test': admin.VERTICAL}


@admin.register(SubjectConsent)
class SubjectConsentAdmin(BaseModelAdmin):

    dashboard_type = 'subject'
    form = SubjectConsentForm
