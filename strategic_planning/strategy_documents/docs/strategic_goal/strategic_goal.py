"""Doc runtime hooks for strategic_goal."""

class DocRuntime:
    doc_key = "strategic_goal"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'activate', 'close', 'defer', 'archive']
