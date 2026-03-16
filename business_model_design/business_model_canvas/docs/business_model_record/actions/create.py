"""Action handler seed for business_model_record:create."""

from __future__ import annotations


DOC_ID = "business_model_record"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'active', 'superseded'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['value_proposition', 'revenue_model', 'model_change_case'], 'borrowed_fields': [], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'update': ['case owner'], 'review': ['case owner'], 'approve': ['case owner'], 'archive': ['case owner']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
