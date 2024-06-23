from dataclasses import dataclass

@dataclass
class User:
    def __init__(self, member_id, firstname, lastname, active, is_pro, gender, email, member_since,
                 timestamp_edit, country, club_id, registration_date, lang, original_member_id, birthday=None):
        self.member_id = member_id
        self.firstname = firstname
        self.lastname = lastname
        self.active = active
        self.is_pro = is_pro
        self.gender = gender
        self.email = email
        self.member_since = member_since
        self.timestamp_edit = timestamp_edit
        self.country = country
        self.club_id = club_id
        self.registration_date = registration_date
        self.lang = lang
        self.original_member_id = original_member_id
        self.birthday = birthday

    def to_dict(self):
        user_dict = {
            "member_id": self.member_id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "active": self.active,
            "is_pro": self.is_pro,
            "gender": self.gender,
            "email": self.email,
            "member_since": self.member_since,
            "timestamp_edit": self.timestamp_edit,
            "country": self.country,
            "club_id": self.club_id,
            "registration_date": self.registration_date,
            "lang": self.lang,
            "original_member_id": self.original_member_id
        }
        if self.birthday:
            user_dict["birthday"] = self.birthday
        return user_dict