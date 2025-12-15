from Repositories.BaseRepository import * 
from  Entities.BaseEntity import *
from DB.SQLiteEngine import SQLiteEngine 
import os
from Config import *
if __name__ == "__main__":
    print(os.getcwd())
    db = SQLiteEngine("./data/clinic.db")
    with open("init.sql", "r") as f:
        sql_contents = f.read()
        db.executescript(sql_contents)
        db.commit()    
    
    patient_repo = PatientRepository(db)
    doctor_repo = DoctorRepository(db)
    appointment_repo = AppointmentRepository(db)

    DEBUG_SQL=False
    # Transaction example
    with db.transaction():
        patient_id1=patient_repo.insert(Patient(full_name="Alice", birth_date='1988-10-09', gender="F", phone="123456"))
        patient_id2=patient_repo.insert(Patient(full_name="Bob", birth_date='1945-09-23', gender="M", phone="789012"))
       
        doctor_id1=doctor_repo.insert(Doctor(full_name="Dr. Smith", speciality="ophthalmology", phone="555-001"))
        doctor_id2=doctor_repo.insert(Doctor(full_name="Dr. Lee", speciality="cardiology", phone="555-002"))
       
        appointment_repo.insert(Appointment(
        patient_id=patient_id1,
        doctor_id=doctor_id1,
        appointment_date="2025-12-20"
        ))
        appointment_repo.insert(Appointment(
            patient_id=patient_id2,
            doctor_id=doctor_id2,
            appointment_date="2025-12-21"
        ))
    
    # doc22=doctor_repo.soft_delete({"doctor_id":12})
    # print(doctor_repo.select_by_id(12))
    
    doctor_repo.hard_delete_by_id(11)
    rows=db.fetch("select * from doctors where doctor_id=11")
    doc11= Doctor(**dict(rows[0])) if rows else None
    print(doc11)
    doctor_repo.soft_delete_by_id(11)
    print(doctor_repo.select_by_id(11))

    # List senior patients
    seniors = patient_repo.get_seniors()
    for p in seniors:
        print(p.full_name,p.birth_date)

    # Count ophthalmology doctors
    count = doctor_repo.count_ophthalmology()
    print("Ophthalmology doctors:", count)

    # print([str(Appointment(**row)) for row in map(dict, db.fetch("select * from appointments"))])
    # print(list( map(dict,db.fetch("select * from appointments"))))
    db.close()