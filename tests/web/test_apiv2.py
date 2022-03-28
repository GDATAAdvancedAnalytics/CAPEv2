import os
import unittest.mock
from unittest.mock import patch

import pytest
from django.test import SimpleTestCase

from lib.cuckoo.core.database import (
    TASK_BANNED,
    TASK_COMPLETED,
    TASK_DISTRIBUTED,
    TASK_DISTRIBUTED_COMPLETED,
    TASK_FAILED_ANALYSIS,
    TASK_FAILED_PROCESSING,
    TASK_FAILED_REPORTING,
    TASK_PENDING,
    TASK_RECOVERED,
    TASK_REPORTED,
    TASK_RUNNING,
    Task,
)


class ReprocessTask(SimpleTestCase):
    @pytest.mark.skip(reason="TODO")
    def test_api_disabled(self):
        patch_target = "lib.cuckoo.common.web_utils.apiconf.taskreprocess"
        with patch.dict(patch_target, {"enabled": False}):
            response = self.client.get("/apiv2/tasks/reprocess/1/")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        json_body = {"error": True, "error_value": "Task Reprocess API is Disabled"}
        assert response.json() == json_body

    @pytest.mark.skip(reason="TODO")
    def test_task_does_not_exist(self):
        patch_target = "lib.cuckoo.core.database.Database.view_task"
        with patch(patch_target, return_value=None):
            response = self.client.get("/apiv2/tasks/reprocess/1/")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        json_body = {"error": True, "error_value": "Task ID does not exist in the database"}
        assert response.json() == json_body

    @pytest.mark.skip(reason="TODO")
    def test_can_reprocess(self):
        task = Task()
        valid_status = (TASK_REPORTED, TASK_RECOVERED, TASK_FAILED_PROCESSING, TASK_FAILED_REPORTING)
        patch_target = "lib.cuckoo.core.database.Database.view_task"
        with patch(patch_target, return_value=task):
            for status in valid_status:
                expected_response = {"error": False, "data": f"Task ID 1 with status {status} marked for reprocessing"}
                with self.subTest(status):
                    task.status = status
                    response = self.client.get("/apiv2/tasks/reprocess/1/")
                    assert response.status_code == 200
                    assert response.headers["content-type"] == "application/json"
                    assert response.json() == expected_response

    @pytest.mark.skip(reason="TODO")
    def test_cant_reprocess(self):
        task = Task()
        invalid_status = (
            TASK_COMPLETED,
            TASK_FAILED_ANALYSIS,
            TASK_DISTRIBUTED_COMPLETED,
            TASK_BANNED,
            TASK_PENDING,
            TASK_RUNNING,
            TASK_DISTRIBUTED,
        )
        patch_target = "lib.cuckoo.core.database.Database.view_task"
        with patch(patch_target, return_value=task):
            for status in invalid_status:
                expected_response = {"error": True, "error_value": f"Task ID 1 cannot be reprocessed in status {status}"}
                with self.subTest(status):
                    task.status = status
                    response = self.client.get("/apiv2/tasks/reprocess/1/")
                    assert response.status_code == 200
                    assert response.headers["content-type"] == "application/json"
                    assert response.json() == expected_response
