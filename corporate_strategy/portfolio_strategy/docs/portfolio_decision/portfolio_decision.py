"""Doc runtime hooks for portfolio_decision."""

class DocRuntime:
    doc_key = "portfolio_decision"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'reject', 'close', 'archive']
