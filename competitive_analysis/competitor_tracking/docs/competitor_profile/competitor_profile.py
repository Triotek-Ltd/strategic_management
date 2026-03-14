"""Doc runtime hooks for competitor_profile."""

class DocRuntime:
    doc_key = "competitor_profile"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
