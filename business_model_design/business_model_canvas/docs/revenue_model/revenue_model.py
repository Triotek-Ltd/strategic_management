"""Doc runtime hooks for revenue_model."""

class DocRuntime:
    doc_key = "revenue_model"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'approve', 'archive']
