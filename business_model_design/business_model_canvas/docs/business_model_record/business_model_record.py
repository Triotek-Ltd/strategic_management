"""Doc runtime hooks for business_model_record."""

class DocRuntime:
    doc_key = "business_model_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'approve', 'archive']
