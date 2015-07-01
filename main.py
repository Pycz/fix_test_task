# coding: utf-8
from string import capwords

from enums import BodyPartType, DanceType

# неким образом полученные данные о танцах - забито пользователем, например
# или из базы данных
dance_data = {
    DanceType.HIPHOP: {
        BodyPartType.BODY: "forward-backward, baby!",
        BodyPartType.HANDS: "bending the elbows!",
        BodyPartType.HEAD: "forward-backward, baby!",
        BodyPartType.LEGS: "crouch! Сrouch!",
    },
    DanceType.ELECTRO: {
        BodyPartType.BODY: "forward-backward, baby!",
        BodyPartType.HANDS: "circle actions!",
        BodyPartType.HEAD: "almost nothing...",
        BodyPartType.LEGS: "in rhythm!",
    },
    DanceType.POP: {
        BodyPartType.BODY: "taking it slooooow.",
        BodyPartType.HANDS: "taking it slooooow.",
        BodyPartType.HEAD: "taking it slooooow.",
        BodyPartType.LEGS: "taking it slooooow.",
    },
}


def get_action(body_part, action_kind):
    """
    Можно сделать класс экшена, но к чему усложнять? В будущем всегда
    можно заменить
    """
    return " ".join((BodyPartType.get_value(body_part), "doing", action_kind))


class Dance(object):
    def __init__(self, _id):
        self.id = _id
        self.name = DanceType.get_value(_id).lower().capitalize()
        self.actions = [get_action(
            *action) for action in dance_data[_id].items()]

    def get_dance_spec(self):
        return "\n".join(self.actions)

avaliable_dances = {dance: Dance(dance) for dance in DanceType.ids}


class Person(object):
    """Нужен пол - добавить в __init__ еще один параметр"""
    def __init__(self, name, dances=None):
        self.name = capwords(name.lower())
        self.dances = []
        if dances:
            self.dances = dances

    def add_dance(self, dance):
        if dance not in self.dances:
            self.dances.append(dance)

    def try_dance(self, dance):
        if not dance:
            print "{0} said this: Silent... Nevermind.".format(self.name)
        elif dance in self.dances:
            dance_spec = avaliable_dances[dance].get_dance_spec()
            print "{0} doing this:\n{1}".format(self.name, dance_spec)
        else:
            print ("{0} said this: Oh, don't my... "
                   "Let's drink some vodka, comrad!".format(self.name))


class Club(object):
    def __init__(self):
        self.persons = []
        self.current_dance = None

    def add_person(self, person_name, dances=None):
        if not dances:
            dances = []
        self.persons.append(Person(person_name, dances))

    def change_dance(self, dance):
        self.current_dance = dance

    def show(self):
        """Показывает состояние клуба"""
        print "==================================="
        print "Now plaing some {0} music!".format(
            DanceType.get_value(self.current_dance) if self.current_dance
            else "silent")
        for person in self.persons:
            person.try_dance(self.current_dance)
            print
        print "==================================="


if __name__ == '__main__':
    club = Club()
    club.show()
    club.add_person("Mike", [DanceType.HIPHOP, DanceType.ELECTRO, ])
    club.show()
    club.add_person("Lili", [DanceType.ELECTRO, ])
    club.show()
    club.add_person("Mr. Smith", [])
    club.show()
    club.add_person("Chuck Norris", [
        DanceType.HIPHOP, DanceType.ELECTRO, DanceType.POP])
    club.show()
    club.change_dance(DanceType.HIPHOP)
    club.show()
    club.change_dance(DanceType.ELECTRO)
    club.show()
    club.change_dance(DanceType.POP)
    club.show()
