"""Action handler seed for revenue_model:review."""

from __future__ import annotations


DOC_ID = "revenue_model"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['business_model_record', 'value_proposition', 'model_change_case'], 'borrowed_fields': ['linked customer scope', 'channel summary from business_model_record'], 'inferred_roles': ['account owner', 'case owner']}, 'actors': ['account owner', 'case owner'], 'action_actors': {'create': ['account owner'], 'update': ['account owner'], 'review': ['case owner'], 'approve': ['case owner'], 'archive': ['account owner']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
