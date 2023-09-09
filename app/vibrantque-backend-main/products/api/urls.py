from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DevicePostView,DeviceStateGetView,GenerateReportView,DeviceNotificationView,DeviceStopPostView,DevicerunnerUnitLimitSwitchStateGetView,DeviceRunnerUnitLimitSwitchView,DeviceRunnerUnitRelay_1View,DeviceRunnerUnitRelay_2View,DeviceRunnerUnitRelay_3View,DeviceRunnerUnitDistanceView,DeviceFloaterUnitLimitSwitchView,DevicefloaterUnitLimitSwitchStateGetView,ReportUpdateViewSet


router = DefaultRouter()
router.register(r'reportupdate', ReportUpdateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('device_start/<id>/',DevicePostView.as_view(),name='device_start'),
    path('device_stop/<id>/',DeviceStopPostView.as_view(),name='device_stop'),
    path('device_state_get/<id>/',DeviceStateGetView.as_view(),name='device_state_get'),
    # path('generate_report/<id>/',GenerateReportView.as_view(),name='generate_report'),
    path('generate_report/',GenerateReportView.as_view(),name='generate_report'),

    path('device_runnerunit_limitswitch_state/<id>/<status>/',DeviceRunnerUnitLimitSwitchView.as_view(),name='device_runnerunit_limitswitch_state'),
    path('device_floaterunit_limitswitch_state/<id>/<status>/',DeviceFloaterUnitLimitSwitchView.as_view(),name='device_floaterunit_limitswitch_state'),
    path('device_floaterunit_limitswitch_state_get/<id>/',DevicefloaterUnitLimitSwitchStateGetView.as_view(),name='device_floaterunit_limitswitch_state_get'),
    path('device_runnerunit_limitswitch_state_get/<id>/',DevicerunnerUnitLimitSwitchStateGetView.as_view(),name='device_runnerunit_limitswitch_state_get'),
    path('device_runnerunit_relay1_state/<id>/<status>/',DeviceRunnerUnitRelay_1View.as_view(),name='device_runnerunit_relay1_state'),
    path('device_runnerunit_relay2_state/<id>/<status>/',DeviceRunnerUnitRelay_2View.as_view(),name='device_runnerunit_relay2_state'),
    path('device_runnerunit_relay3_state/<id>/<status>/',DeviceRunnerUnitRelay_3View.as_view(),name='device_runnerunit_relay3_state'),
    path('device_runnerunit_distance_state/<id>/<status>/',DeviceRunnerUnitDistanceView.as_view(),name='device_runnerunit_distance_state'),
    path('device_notification/<id>/<status>/',DeviceNotificationView.as_view(),name='device_runnerunit_distance_state'),

]

