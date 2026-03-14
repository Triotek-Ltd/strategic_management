"""Doc runtime hooks for strategic_risk_signal."""

class DocRuntime:
    doc_key = "strategic_risk_signal"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'mitigate', 'escalate', 'close', 'archive']
