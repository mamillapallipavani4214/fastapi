from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






@app.post("/mobiles", response_model=schemas.mobileResponse)
def create(mobile: schemas.mobileCreate, db: Session = Depends(get_db)):
    return crud.create_mobile(db, mobile)

@app.get("/mobiles", response_model=list[schemas.mobileResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_mobiles(db)

@app.get("/mobiles/{mobile_id}", response_model=schemas.mobileResponse)
def read_one(mobile_id: int, db: Session = Depends(get_db)):
    mobile = crud.get_mobile(db, mobile_id)
    if not mobile:
        raise HTTPException(status_code=404, detail="mobile not found")
    return mobile

@app.put("/mobiles/{mobile_id}", response_model=schemas.mobileResponse)
def update(mobile_id: int, mobile: schemas.mobileCreate, db: Session = Depends(get_db)):
    updated = crud.update_mobile(db, mobile_id, mobile)
    if not updated:
        raise HTTPException(status_code=404, detail="mobile not found")
    return updated

@app.delete("/mobiles/{mobile_id}")
def delete(mobile_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_mobile(db, mobile_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="mobile not found")
    return {"message":"mobile deleted successfully"}




@app.get("/dept/{dept}")
def get_dept_mob(dept:str,db:Session=Depends(get_db)):
    return crud.get_emp_by_dept(db,dept)