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

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from wger.core.models import UserProfile


class AddUserRestApiTestCase(TestCase):
    '''
    Test that a user can receive auth to create another user.
    '''

    def test_add_user_rest_api(self):
        user = User.objects.create(username='somefella')
        user_profile = UserProfile.objects.get(user=user)

        self.assertFalse(user_profile.can_create_via_api)

        call_command('add-user-rest-api', 'somefella')
        user_profile.refresh_from_db()

        self.assertTrue(user_profile.can_create_via_api)
