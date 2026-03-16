"""Action handler seed for model_change_case:approve."""

from __future__ import annotations


DOC_ID = "model_change_case"
ACTION_ID = "approve"
ACTION_RULE = {'allowed_in_states': ['proposed', 'in_review', 'approved', 'rejected'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['business_model_record', 'value_proposition', 'revenue_model'], 'borrowed_fields': ['current model details from business_model_record'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'submit': ['case owner'], 'review': ['case owner'], 'approve': ['case owner'], 'reject': ['case owner'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
