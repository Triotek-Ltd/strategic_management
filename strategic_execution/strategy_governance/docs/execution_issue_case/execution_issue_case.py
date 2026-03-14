"""Doc runtime hooks for execution_issue_case."""

class DocRuntime:
    doc_key = "execution_issue_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'mitigate', 'escalate', 'close', 'archive']
