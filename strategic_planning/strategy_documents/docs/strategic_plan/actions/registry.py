"""Action registry seed for strategic_plan."""

from __future__ import annotations


DOC_ID = "strategic_plan"
ALLOWED_ACTIONS = ['create', 'update', 'review', 'approve', 'publish', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'active', 'superseded'], 'transitions_to': None}, 'update': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'active', 'superseded'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'active', 'superseded'], 'transitions_to': 'reviewed'}, 'approve': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'active', 'superseded'], 'transitions_to': 'approved'}, 'publish': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'active', 'superseded'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'active', 'superseded'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
