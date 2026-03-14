"""Doc runtime hooks for value_proposition."""

class DocRuntime:
    doc_key = "value_proposition"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'publish', 'archive']
