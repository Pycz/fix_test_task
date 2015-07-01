# coding: utf-8
"""Чтобы строками не манипулировать
"""
body_parts = ("Body", "Hands", "Head", "Legs")

class BaseEnum(object):
    ids = ()
    values = {}

    @classmethod
    def get_value(cls, _id):
        return cls.values[_id]

class BodyPartType(BaseEnum):
    ids = range(1, 5)
    BODY, HANDS, HEAD, LEGS = ids
    values = {
        BODY: "Body",
        HANDS: "Hands",
        HEAD: "Head",
        LEGS: "Legs",
    }

dances = ("Hip-hop", "Electrodance", "Pop")

class DanceType(BaseEnum):
    ids = range(1, 4)
    HIPHOP, ELECTRO, POP = ids
    values = {
        HIPHOP: "Hip-hop",
        ELECTRO: "Electrodance",
        POP: "Pop",
    }
