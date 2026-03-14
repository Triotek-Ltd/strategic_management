"""Doc runtime hooks for growth_initiative."""

class DocRuntime:
    doc_key = "growth_initiative"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'approve', 'activate', 'close', 'stop', 'archive']
