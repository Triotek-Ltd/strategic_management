"""Doc runtime hooks for corporate_strategy_record."""

class DocRuntime:
    doc_key = "corporate_strategy_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'approve', 'archive']
