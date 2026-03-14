"""Doc runtime hooks for planning_cycle."""

class DocRuntime:
    doc_key = "planning_cycle"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'activate', 'close', 'archive']
