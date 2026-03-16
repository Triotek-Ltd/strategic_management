"""Action handler seed for strategic_risk_signal:mitigate."""

from __future__ import annotations


DOC_ID = "strategic_risk_signal"
ACTION_ID = "mitigate"
ACTION_RULE = {'allowed_in_states': ['raised', 'reviewed', 'mitigating', 'escalated'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['market_analysis', 'competitive_observation', 'execution_issue_case'], 'borrowed_fields': ['source context from market_analysis or competitive_observation'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'assign': ['case owner'], 'review': ['case owner'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_mitigate(payload: dict, context: dict | None = None) -> dict:
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
