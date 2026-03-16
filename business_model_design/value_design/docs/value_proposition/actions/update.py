"""Action handler seed for value_proposition:update."""

from __future__ import annotations


DOC_ID = "value_proposition"
ACTION_ID = "update"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['business_model_record', 'revenue_model'], 'borrowed_fields': ['customer scope from business_model_record'], 'inferred_roles': ['account owner']}, 'actors': ['account owner'], 'action_actors': {'create': ['account owner'], 'update': ['account owner'], 'review': ['account owner'], 'publish': ['account owner'], 'archive': ['account owner']}}

def handle_update(payload: dict, context: dict | None = None) -> dict:
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
