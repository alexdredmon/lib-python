from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import JSON


def JsonColumn(**kwargs):
    return Column(JSON, **kwargs)


def StringColumn(length=50, **kwargs):
    return Column(
        String(length),
        **kwargs
    )
