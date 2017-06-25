from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('firstname', VARCHAR(length=120)),
    Column('lastname', VARCHAR(length=120)),
    Column('email', VARCHAR(length=120)),
    Column('reason', VARCHAR(length=240)),
)

staff = Table('staff', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('firstname', String(length=142), nullable=False),
    Column('lastname', String(length=142), nullable=False),
    Column('role', String(length=16)),
    Column('slack', String(length=16)),
    Column('email', String(length=142)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].drop()
    post_meta.tables['staff'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].create()
    post_meta.tables['staff'].drop()
