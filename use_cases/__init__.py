"""use cases"""

from use_cases.issues import IssuesUseCases
from storage.issues.in_memory_db import TodoInMemoryDatabaseService

database_service = TodoInMemoryDatabaseService()
issues_use_cases = IssuesUseCases(database_service=database_service)
