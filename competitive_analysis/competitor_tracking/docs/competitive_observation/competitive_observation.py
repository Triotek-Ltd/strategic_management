"""Doc runtime hooks for competitive_observation."""

class DocRuntime:
    doc_key = "competitive_observation"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
