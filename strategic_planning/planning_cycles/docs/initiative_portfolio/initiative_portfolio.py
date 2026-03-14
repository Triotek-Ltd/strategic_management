"""Doc runtime hooks for initiative_portfolio."""

class DocRuntime:
    doc_key = "initiative_portfolio"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'rebalance', 'close', 'archive']
