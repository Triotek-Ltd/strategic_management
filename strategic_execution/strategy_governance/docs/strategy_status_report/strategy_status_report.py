"""Doc runtime hooks for strategy_status_report."""

class DocRuntime:
    doc_key = "strategy_status_report"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'publish', 'archive']
