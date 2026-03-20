"""Action handler seed for revenue_model:create."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "revenue_model"
ACTION_ID = "create"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'approved', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['business_model_record', 'value_proposition', 'model_change_case'], 'borrowed_fields': ['linked customer scope', 'channel summary from business_model_record'], 'inferred_roles': ['account owner', 'case owner']}, 'actors': ['account owner', 'case owner'], 'action_actors': {'create': ['account owner'], 'update': ['account owner'], 'review': ['case owner'], 'approve': ['case owner'], 'archive': ['account owner']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['draft', 'approved', 'active'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_create(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "action_contract": ACTION_CONTRACT,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
