from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class TimestampMixin:
    """
    Adds automatic created_at and updated_at fields
    to any model that inherits from this mixin.
    """

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )