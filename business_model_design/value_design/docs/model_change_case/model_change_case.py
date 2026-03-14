"""Doc runtime hooks for model_change_case."""

class DocRuntime:
    doc_key = "model_change_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'review', 'approve', 'reject', 'close', 'archive']
