from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Database connection
db = create_engine('sqlite:///sqlite.db')

# Construct a base class for declarative class definitions
Base = declarative_base()
