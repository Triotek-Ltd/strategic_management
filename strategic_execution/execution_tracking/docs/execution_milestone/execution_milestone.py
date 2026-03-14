"""Doc runtime hooks for execution_milestone."""

class DocRuntime:
    doc_key = "execution_milestone"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'delay', 'close', 'archive']
