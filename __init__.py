from mycroft import MycroftSkill, intent_file_handler


class DoctorV(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('v.doctor.intent')
    def handle_v_doctor(self, message):
        self.speak_dialog('v.doctor')


def create_skill():
    return DoctorV()

