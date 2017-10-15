from sqlalchemy import func, and_
from main import db

def ifilter_by(class_type, **kwargs):
    filters = []
    for attr, value in kwargs.items():
        if hasattr(class_type, attr):
            col = getattr(class_type, attr)
            if isinstance(col.type, db.String):
                filters.append(col.ilike(value))
            else:
                filters.append(col == value)
    return and_(*filters)
