from sqlalchemy.orm import sessionmaker, scoped_session
from .engine import get_engine

# Create a session factory using the engine
SessionFactory = sessionmaker(bind=get_engine(), autoflush=False, autocommit=False)

# Define a thread-local session to ensure session safety in multi-threaded applications
ScopedSession = scoped_session(SessionFactory)

def get_session():
    """
    Returns a new session instance for database operations.
    :return: ScopedSession instance
    """
    return ScopedSession()

def get_base_session():
    """
    Returns the raw session factory for customized usage.
    :return: SessionFactory
    """
    return SessionFactory()
