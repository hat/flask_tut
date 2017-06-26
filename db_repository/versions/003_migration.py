from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
guests = Table('guests', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('firstname', String(length=142), nullable=False),
    Column('lastname', String(length=142), nullable=False),
    Column('timein', DateTime, nullable=False),
    Column('timeout', DateTime),
    Column('reason', String(length=255)),
    Column('photo', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['guests'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['guests'].drop()
