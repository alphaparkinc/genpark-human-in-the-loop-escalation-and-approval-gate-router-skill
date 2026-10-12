"""Human-in-the-Loop Escalation & Approval Gate Router.
100% Python Standard Library.
"""

class HumanInTheLoopApprovalGate:
    """Evaluates action financial impact, reversibility, and PII sensitivity to route high-risk agent actions to human approval."""

    @staticmethod
    def evaluate_approval_gate(action_name: str, monetary_value_usd: float, is_reversible: bool, touches_pii: bool) -> dict:
        reasons = []
        if monetary_value_usd >= 250.0:
            reasons.append(f"Monetary impact (${monetary_value_usd:.2f}) exceeds autonomous threshold ($250.00).")
        if not is_reversible:
            reasons.append("Action is irreversible and modifies external production state.")
        if touches_pii:
            reasons.append("Action accesses or mutates regulated PII fields.")

        requires_approval = len(reasons) > 0
        tier = "EXECUTIVE_APPROVAL" if monetary_value_usd >= 1000.0 else ("OPERATOR_APPROVAL" if requires_approval else "AUTO_APPROVED")

        return {
            "action_name": action_name,
            "approval_tier": tier,
            "requires_human_signoff": requires_approval,
            "escalation_reasons": reasons
        }
