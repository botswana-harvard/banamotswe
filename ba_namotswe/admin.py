from django.contrib import admin

from .admin_site import ba_namotswe_admin
from .models import (
    RegisteredSubject, SubjectVisit, Enrollment, Io, Abstraction, Treatment, ARTRegimen, Appointment)
from ba_namotswe.forms.enrollment_form import EnrollmentForm
from ba_namotswe.forms.registered_subject_form import RegisteredSubjectForm
<<<<<<< HEAD
=======
from ba_namotswe.forms.treatment_form import TreatmentForm
>>>>>>> 4265853bf8180eca6fa9f32bcd6ef09d9e7b2d64


@admin.register(Enrollment, site=ba_namotswe_admin)
class EnrollmentAdmin(admin.ModelAdmin):
    form = EnrollmentForm
    radio_fields = {
        'caregiver_relation': admin.VERTICAL,
        'weight_measured': admin.VERTICAL,
        'height_measured': admin.VERTICAL}


@admin.register(RegisteredSubject, site=ba_namotswe_admin)
class RegisteredSubjectAdmin(admin.ModelAdmin):
    list_filter = ('dob', )
    form = RegisteredSubjectForm


@admin.register(Appointment, site=ba_namotswe_admin)
class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ('best_appt_datetime', )


@admin.register(SubjectVisit, site=ba_namotswe_admin)
class SubjectVisitAdmin(admin.ModelAdmin):
    list_filter = ('report_datetime', )


@admin.register(Abstraction, site=ba_namotswe_admin)
class AbstractionAdmin(admin.ModelAdmin):
    list_filter = ('subject_visit', )


@admin.register(Treatment, site=ba_namotswe_admin)
class TreatmentAdmin(admin.ModelAdmin):
    list_filter = ('perinatal_infection', )
    form = TreatmentForm


@admin.register(Io, site=ba_namotswe_admin)
class IoAdmin(admin.ModelAdmin):
    list_filter = ('name', )


@admin.register(ARTRegimen, site=ba_namotswe_admin)
class ARTRegimenAdmin(admin.ModelAdmin):
    list_filter = ('name', )
