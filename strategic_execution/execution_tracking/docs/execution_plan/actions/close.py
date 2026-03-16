"""Action handler seed for execution_plan:close."""

from __future__ import annotations


DOC_ID = "execution_plan"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'active', 'revised', 'completed'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['growth_initiative', 'execution_milestone', 'strategy_status_report', 'execution_issue_case'], 'borrowed_fields': ['strategic priorities from growth_initiative or corporate_strategy_record'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'update': ['case owner'], 'review': ['case owner'], 'approve': ['case owner'], 'activate': ['case owner'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_close(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
