from datetime import datetime
from typing import Any, Dict, TypeVar, Generic

T=TypeVar("T")
class BaseEntity(Generic[T]):
    #Base entity class containing audit fields and soft delete flag.
    def __init__(self, create_time=None, modify_time=None, is_deleted=0):
        self.create_time = create_time or datetime.now()
        self.modify_time = modify_time or datetime.now()
        self.is_deleted = is_deleted

    def __str__(self) -> str:
        # Generic human-readable string representation.
        # Automatically works for all child entities.
        attrs = ", ".join(
            f"{key}={value}"
            for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({attrs})"

class Patient(BaseEntity["Patient"]):
    def __init__(self, patient_id=None, full_name=None, birth_date=None, gender=None, phone=None, **kwargs):
        self.patient_id = patient_id
        self.full_name = full_name
        self.birth_date = birth_date
        self.gender = gender
        self.phone = phone
        super().__init__(**kwargs)
    
class Doctor(BaseEntity["Doctor"]):
    def __init__(self, doctor_id=None, full_name=None, speciality=None, phone=None, **kwargs):
        self.doctor_id = doctor_id
        self.full_name = full_name
        self.speciality = speciality
        self.phone = phone
        super().__init__(**kwargs)

class Appointment(BaseEntity["Appointment"]):
    def __init__(self, appointment_id=None, patient_id=None, doctor_id=None, appointment_date=None, **kwargs):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        super().__init__(**kwargs)
    