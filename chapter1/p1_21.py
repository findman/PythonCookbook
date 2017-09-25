#!/usr/bin/env python3
# -*- coding:utf8 -*-

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
users = sorted(users,key=lambda u:u.user_id)
print(users)
