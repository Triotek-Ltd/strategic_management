"""Doc runtime hooks for market_analysis."""

class DocRuntime:
    doc_key = "market_analysis"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'publish', 'archive']
