# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file "docs/LICENSE" for copying permission.

from __future__ import absolute_import

from apiv2 import views
from django.conf.urls import include, re_path
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path(r"^$", views.index, name="apiv2"),
    # disabled due to token auth
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    re_path(r"^tasks/create/file/$", views.tasks_create_file),
    re_path(r"^tasks/stats/$", views.task_x_hours),
    re_path(r"^tasks/create/url/$", views.tasks_create_url),
    re_path(r"^tasks/create/dlnexec/$", views.tasks_create_dlnexec),
    re_path(r"^tasks/create/vtdl/$", views.tasks_vtdl),
    re_path(r"^tasks/create/static/$", views.tasks_create_static),
    re_path(r"^tasks/search/md5/(?P<md5>([a-fA-F\d]{32}))/$", views.tasks_search),
    re_path(r"^tasks/search/sha1/(?P<sha1>([a-fA-F\d]{40}))/$", views.tasks_search),
    re_path(r"^tasks/search/sha256/(?P<sha256>([a-fA-F\d]{64}))/$", views.tasks_search),
    re_path(r"^tasks/extendedsearch/$", views.ext_tasks_search),
    re_path(r"^tasks/list/$", views.tasks_list),
    re_path(r"^tasks/list/(?P<limit>\d+)/$", views.tasks_list),
    re_path(r"^tasks/list/(?P<limit>\d+)/(?P<offset>\d+)/$", views.tasks_list),
    re_path(r"^tasks/list/(?P<limit>\d+)/(?P<offset>\d+)/(?P<window>\d+)/$", views.tasks_list),
    re_path(r"^tasks/view/(?P<task_id>\d+)/$", views.tasks_view),
    re_path(r"^tasks/reschedule/(?P<task_id>\d+)/$", views.tasks_reschedule),
    re_path(r"^tasks/reprocess/(?P<task_id>\d+)/$", views.tasks_reprocess),
    re_path(r"^tasks/delete/(?P<task_id>(\d+|[0-9,]+))/$", views.tasks_delete),
    re_path(r"^tasks/delete/(?P<task_id>\d+)/(?P<status>\w+)/$", views.tasks_delete),
    re_path(r"^tasks/delete_many/$", views.tasks_delete_many),
    re_path(r"^tasks/status/(?P<task_id>\d+)/$", views.tasks_status),
    re_path(r"^tasks/get/report/(?P<task_id>\d+)/$", views.tasks_report),
    re_path(r"^tasks/get/report/(?P<task_id>\d+)/(?P<report_format>\w+)/$", views.tasks_report),
    re_path(r"^tasks/get/report/(?P<task_id>\d+)/(?P<report_format>\w+)/(?P<make_zip>\w{3})/$", views.tasks_report),
    re_path(r"^tasks/get/iocs/(?P<task_id>\d+)/$", views.tasks_iocs),
    re_path(r"^tasks/get/iocs/(?P<task_id>\d+)/(?P<detail>detailed)/$", views.tasks_iocs),
    re_path(r"^tasks/get/config/(?P<task_id>\d+)/$", views.tasks_config),
    re_path(r"^tasks/get/config/(?P<task_id>\d+)/(?P<cape_name>\w+)/$", views.tasks_config),
    re_path(r"^tasks/get/screenshot/(?P<task_id>\d+)/$", views.tasks_screenshot),
    re_path(r"^tasks/get/screenshot/(?P<task_id>\d+)/(?P<screenshot>\d{1,4})/$", views.tasks_screenshot),
    re_path(r"^tasks/get/procmemory/(?P<task_id>\d+)/$", views.tasks_procmemory),
    re_path(r"^tasks/get/procmemory/(?P<task_id>\d+)/(?P<pid>\d{1,5})/$", views.tasks_procmemory),
    re_path(r"^tasks/get/fullmemory/(?P<task_id>\d+)/$", views.tasks_fullmemory),
    re_path(r"^tasks/get/pcap/(?P<task_id>\d+)/$", views.tasks_pcap),
    re_path(r"^tasks/get/dropped/(?P<task_id>\d+)/$", views.tasks_dropped),
    re_path(r"^tasks/get/surifile/(?P<task_id>\d+)/$", views.tasks_surifile),
    re_path(r"^tasks/get/payloadfiles/(?P<task_id>\d+)/$", views.tasks_payloadfiles),
    re_path(r"^tasks/get/procdumpfiles/(?P<task_id>\d+)/$", views.tasks_procdumpfiles),
    re_path(r"^files/view/md5/(?P<md5>([a-fA-F\d]{32}))/$", views.files_view),
    re_path(r"^files/view/sha1/(?P<sha1>([a-fA-F\d]{40}))/$", views.files_view),
    re_path(r"^files/view/sha256/(?P<sha256>([a-fA-F\d]{64}))/$", views.files_view),
    re_path(r"^files/view/id/(?P<sample_id>\d+)/$", views.files_view),
    re_path(r"^files/get/(?P<stype>md5)/(?P<value>([a-fA-F\d]{32}))/$", views.file),
    re_path(r"^files/get/(?P<stype>sha1)/(?P<value>([a-fA-F\d]{40}))/$", views.file),
    re_path(r"^files/get/(?P<stype>sha256)/(?P<value>([a-fA-F\d]{64}))/$", views.file),
    re_path(r"^files/get/(?P<stype>task)/(?P<value>\d+)/$", views.file),
    re_path(r"^machines/list/$", views.machines_list),
    re_path(r"^machines/view/(?P<name>[\w$-/:-?{-~!^_`\[\]]+)/$", views.machines_view),
    re_path(r"^cuckoo/status/$", views.cuckoo_status),
    re_path(r"^tasks/get/rollingsuri/(?P<window>\d+)/$", views.tasks_rollingsuri),
    re_path(r"^tasks/get/rollingshrike/(?P<window>\d+)/$", views.tasks_rollingshrike),
    re_path(r"^tasks/get/rollingshrike/(?P<window>\d+)/(?P<msgfilter>[\w$-/:-?{-~!^_`\[\]\s\x5c]+)/$", views.tasks_rollingshrike),
    re_path(r"^tasks/get/latests/(?P<hours>\d+)/$", views.tasks_latest),
    # re_path(r"^tasks/add/(?P<category>[A-Za-z0-9]+)/(?P<task_id>\d+)/$", views.post_processing),
    re_path(r"^tasks/statistics/(?P<days>\d+)/$", views.statistics_data),
    re_path(r"^exitnodes/$", views.exit_nodes_list),
]
