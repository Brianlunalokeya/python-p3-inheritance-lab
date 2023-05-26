#!/usr/bin/env python

from user import User

from random import choice

class Teacher(User):
    def __init__(self, first_name, last_name):
        super(Teacher, self).__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        return choice(self.knowledge)