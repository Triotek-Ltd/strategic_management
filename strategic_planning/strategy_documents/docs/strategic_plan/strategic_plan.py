"""Doc runtime hooks for strategic_plan."""

class DocRuntime:
    doc_key = "strategic_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'approve', 'publish', 'archive']
