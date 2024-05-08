from typing import List, Optional
from datetime import date, timedelta
from sqlalchemy import extract, and_, or_
from sqlalchemy.orm import Session
from src.database.models import Contact
from src.schemas import ContactModel, ContactUpdate


async def get_contacts(skip: int,
                       limit: int,
                       search: str,
                       db: Session) -> List[Contact]:
    query = db.query(Contact)
    if search:
        query = query.filter(
            (Contact.first_name.ilike(f'%{search}%')) |
            (Contact.last_name.ilike(f'%{search}%')) |
            (Contact.email.ilike(f'%{search}%')) |
            (Contact.phone_number.ilike(f'%{search}%'))
        )
    return query.offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name,
                      last_name=body.last_name,
                      email=body.email,
                      phone_number=body.phone_number,
                      birthday=body.birthday,
                      additional_info=body.additional_info
                      )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int,
                         body: ContactUpdate,
                         db: Session) -> Optional[Contact]:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        update_data = body.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(contact, key, value)
        db.commit()
    return contact


async def get_upcoming_birthdays(db: Session, today: date) -> List[Contact]:
    in_a_week = today + timedelta(days=7)
    if today.month == in_a_week.month:
        return db.query(Contact).filter(
            and_(
                extract('month', Contact.birthday) == today.month,
                extract('day', Contact.birthday) >= today.day,
                extract('day', Contact.birthday) <= in_a_week.day
            )
        ).all()
    else:
        return db.query(Contact).filter(
            or_(
                and_(
                    extract('month', Contact.birthday) == today.month,
                    extract('day', Contact.birthday) >= today.day
                ),
                and_(
                    extract('month', Contact.birthday) == in_a_week.month,
                    extract('day', Contact.birthday) <= in_a_week.day
                )
            )
        ).all()
