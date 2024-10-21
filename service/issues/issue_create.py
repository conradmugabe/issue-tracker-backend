"""Issue service"""

from models.issues import (
    Validator,
    Storage,
    Issue,
    CreateIssue,
)

from models.common import IdGenerator


class IssueCreate:
    """Issue service"""

    def __init__(
        self,
        storage: Storage,
        validator: Validator,
        id_generator: IdGenerator,
    ):
        self.storage = storage
        self.validator = validator
        self.id_generator = id_generator

    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""
        valid = self.validator.validate_create_issue(data)
        if not valid:
            raise ValueError(
                "invalid issue data"
            )  # or handle in chosen error handling style

        issue = Issue()
        issue.id = self.id_generator.generate()
        issue.title = f"t-{data.title}"

        self.storage.save_issue(issue)

        return issue
