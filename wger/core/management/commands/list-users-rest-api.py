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

from django.core.management.base import BaseCommand
from wger.core.models import UserProfile


class Command(BaseCommand):
    '''
    Command to list all the users created by a certain user
    '''

    help = 'List all users created by another user'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='?', type=str)

    def handle(self, **options):

        username = options.get("username", None)

        try:
            users = UserProfile.objects.all().filter(created_by=username)
            if len(users) < 1:
                return 'No users created by {}'.format(username)

            elif len(users) > 0:
                print('The users created by {} are: '.format(username))
                for user in users:
                    print('\t' + user.username)

        except Exception:
            print('User {} not found'.format(username))
