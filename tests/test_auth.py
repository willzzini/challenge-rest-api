# coding: utf-8
import os
import json
import requests
import unittest

from tests.test_setup import TestSetup, \
    URL_LOCALHOST

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'integration_variables.json')
with open(file_path) as variable_file:
    data = json.load(variable_file)

USER_INFO = data.get("register")


class TestAdminEndpoint(unittest.TestCase):
    def setUp(self):
        self.initial_setup = TestSetup()

        self.setup_localhost = self.initial_setup.setup_user_localhost()
        self.auth_localhost = json.loads(self.setup_localhost.text)
        self.token_localhost = self.auth_localhost.get("tokens")

    def test_01_localhost_register(self):
        for key, value in self.token_stag.items():
            create_endpoint = requests.post(
                URL_LOCALHOST +
                "/register",
                data=USER_INFO,
                headers={"Authentication-Token": value})
            create_endpoint_user_exist = requests.post(
                URL_LOCALHOST +
                "/register",
                data=USER_INFO,
                headers={"Authentication-Token": value})

            self.assertEqual(403, create_endpoint.status_code)
            self.assertEqual(403, create_endpoint_user_exist.status_code)
