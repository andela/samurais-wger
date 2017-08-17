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
import sys

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from wger.core.models import UserProfile

try:
    # Python 2
    from cStringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO



class ListApiUsersTestCase(TestCase):
    '''
    Test that a user can list all users created via the REST API.
    '''

    def test_list_user_rest_api(self):
        creator = User.objects.create(username='creator')

        user1 = User.objects.create(username='randomdude')
        user1_profile = UserProfile.objects.get(user=user1)
        user1_profile.created_by = creator.username
        user1_profile.save()
        user1_profile.refresh_from_db()

        user2 = User.objects.create(username='randomdudette')
        user2_profile = UserProfile.objects.get(user=user2)
        user2_profile.created_by = creator.username
        user2_profile.save()
        user2_profile.refresh_from_db()

        held = sys.stdout
        sys.stdout = StringIO()

        call_command(
            'list-users-rest-api', 'creator')

        data = sys.stdout.getvalue().strip()
        sys.stdout = held

        self.assertIn('randomdude', str(data))
        self.assertIn('randomdudette', data)
