"""Doc runtime hooks for execution_plan."""

class DocRuntime:
    doc_key = "execution_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'approve', 'activate', 'close', 'revise', 'archive']
