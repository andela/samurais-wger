# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
import json

from django.contrib.auth.models import User
from django.test import Client
from rest_framework import status
from wger.core.models import UserProfile
from wger.core.tests.base_testcase import WorkoutManagerTestCase


class ApiUserTestCase(WorkoutManagerTestCase):
    '''
     Test API user creation
    '''

    def test_create_user_via_api(self):
        '''
        Tests the creation of a user via the API
        '''
        user = User.objects.create_user(
            username='pmusonye',
            password='password')
        user.save()
        profile = UserProfile.objects.get(user=user)
        profile.can_create_via_api = True
        profile.save()

        self.client = Client()
        self.client.login(username='pmusonye', password='password')

        payload = {
            'username': 'jdoe',
            'email': 'jdoe@gmail.com',
            'password': 'password'
        }

        create = self.client.post(
            '/api/v2/usercreation/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        doe = User.objects.get(username='jdoe')
        doe_profile = UserProfile.objects.get(user=doe)

        self.assertEqual(doe_profile.created_by, 'pmusonye')
        self.assertEqual(create.status_code, status.HTTP_201_CREATED)
