from .adminHelpers import *
from .basic import *
from .expand import *
from .interval import *
from .msg_types import *
from .parser import *
from .PyroHelpers import *
from .tools import *
from .utility import *

import os
import motor.motor_asyncio
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URL = "postgres://cnblatro:BffSNIY-ZHwVGU75Xcd_TE2EaINGQvgE@tiny.db.elephantsql.com/cnblatro"

SPAMBOT = "SPAMBOT"


def start() -> scoped_session:
    engine = create_engine(DB_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(e)


DB_AVAILABLE = False
BOTINLINE_AVAIABLE = False


def mulaisql() -> scoped_session:
    global DB_AVAILABLE
    engine = create_engine(DB_URL, client_encoding="utf8")
    BASE.metadata.bind = engine
    try:
        BASE.metadata.create_all(engine)
    except exc.OperationalError:
        DB_AVAILABLE = False
        return False
    DB_AVAILABLE = True
    return scoped_session(sessionmaker(bind=engine, autoflush=False))
