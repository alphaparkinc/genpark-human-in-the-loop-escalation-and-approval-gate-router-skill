"""Example usage for Human-in-the-Loop Escalation & Approval Gate Router."""
from client import HumanInTheLoopApprovalGate

if __name__ == "__main__":
    res = HumanInTheLoopApprovalGate.evaluate_approval_gate("issue_refund", 450.0, False, True)
    print("Approval Tier:", res["approval_tier"])
    print("Reasons:", res["escalation_reasons"])
