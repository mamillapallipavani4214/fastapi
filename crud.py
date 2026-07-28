from sqlalchemy.orm import Session
import models
import schemas

def create_mobile(db: Session, mobile: schemas.mobileCreate):
    #creating  a mobile object with user values
    db_mobile = models.mobile(**mobile.model_dump())
    #adding new mobile to existing table
    db.add(db_mobile)
    #commiting the changes to the database
    db.commit()
    #refreshing the database to get updated values
    db.refresh(db_mobile)
    #returning response to the user
    return db_mobile

def get_mobiles(db: Session):


    return db.query(models.mobile).all()

def get_mobile(db: Session, mobile_id: int):
    return db.query(models.mobile).filter(
        models.mobile.id == mobile_id
    ).first()

def update_mobile(db: Session, mobile_id: int, mobile: schemas.mobileCreate):
    db_mobile = get_mobile(db, mobile_id)
    if not db_mobile:
        return None
    db_mobile.name = mobile.name
    db_mobile.department=mobile.department 
    db_mobile.email=mobile.email
    db_mobile.location=mobile.location

    db.commit()
    db.refresh(db_mobile)
    return db_mobile

def delete_mobile(db: Session, mobile_id: int):
    db_mobile = get_mobile(db, mobile_id)
    if not db_mobile:
        return None
    db.delete(db_mobile)
    db.commit()
    return db_mobile



def get_emp_by_dept(db:Session,dept:str):
    print(dept)
    return db.query(models.mobile).filter(
         models.mobile.department==dept
    ).all()



    

