from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.visit import Crf
from edc_visit_schedule.visit_schedule import VisitSchedule

entry_to_care_crfs = (
    Crf(show_order=10, model='ba_namotswe.entrytocare'),
    Crf(show_order=20, model='ba_namotswe.whostaging'),
    Crf(show_order=30, model='ba_namotswe.adherencecounselling'),
    Crf(show_order=40, model='ba_namotswe.pregnancyhistory'),
    Crf(show_order=50, model='ba_namotswe.artrecord'),
    Crf(show_order=60, model='ba_namotswe.labrecord'),
    Crf(show_order=70, model='ba_namotswe.oirecord'),
    Crf(show_order=80, model='ba_namotswe.tbrecord'),
    Crf(show_order=90, model='ba_namotswe.transferrecord'),
)

in_care_crfs = (
    Crf(show_order=10, model='ba_namotswe.incare'),
    Crf(show_order=30, model='ba_namotswe.adherencecounselling'),
    Crf(show_order=40, model='ba_namotswe.pregnancyhistory'),
    Crf(show_order=50, model='ba_namotswe.artrecord'),
    Crf(show_order=60, model='ba_namotswe.labrecord'),
    Crf(show_order=70, model='ba_namotswe.oirecord'),
    Crf(show_order=80, model='ba_namotswe.tbrecord'),
    Crf(show_order=90, model='ba_namotswe.transferrecord'),
)

requisitions = ()

visit_schedule = VisitSchedule(
    name='visit_schedule',
    verbose_name='Ba Namotswe Visit Schedule',
    app_label='ba_namotswe',
    visit_model='ba_namotswe.subjectvisit',
    enrollment_model='ba_namotswe.enrollment',
    disenrollment_model='ba_namotswe.disenrollment',
    offstudy_model='ba_namotswe.subjectoffstudy',
)

# add schedules
schedule = Schedule(name='schedule')

schedule.add_visit(
    code='1000',
    title='Patient History and Entry into Care',
    timepoint=0,
    base_interval=0,
    requisitions=requisitions,
    crfs=entry_to_care_crfs)

for i in range(1, 11):
    schedule.add_visit(
        code=str(1000 + (10 * i)),
        title='In-care visit',
        timepoint=i * 10,
        base_interval=i,
        requisitions=requisitions,
        crfs=in_care_crfs)

visit_schedule.add_schedule(schedule)

site_visit_schedules.register(visit_schedule)
