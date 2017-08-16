# -*- coding: utf-8 *-*

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
from django.core.management.base import BaseCommand
from wger.core.models import UserProfile


class Command(BaseCommand):
    '''
    Command to allow other apps/users to create users via the REST API
    '''

    help = 'Allow other apps/users to create users via the REST API'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='?', type=str)

    def handle(self, **options):
        '''
        Find if the currently the consumer can create users
        '''
        username = options.get("username", None)
        try:
            user = User.objects.get(username=username)
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.can_create_via_api:
                return ('{} is already allowed to create users via the API'
                        .format(user.username))
            else:
                user_profile.can_create_via_api = True

                user_profile.save()
                return ('Successfully allowed {} to create users via the API'
                        .format(user.username))

        except Exception:
            print('User {} not found'.format(username))
