"""Doc runtime hooks for strategy_review_note."""

class DocRuntime:
    doc_key = "strategy_review_note"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
