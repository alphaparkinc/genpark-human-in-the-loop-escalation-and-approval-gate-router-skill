"""MCP server for Human-in-the-Loop Escalation & Approval Gate Router."""
import sys
import json
from client import HumanInTheLoopApprovalGate

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "evaluate_hitl_approval_gate",
                "description": "Determines whether an autonomous action requires human operator or executive sign-off",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action_name": {"type": "string"},
                        "monetary_value_usd": {"type": "number"},
                        "is_reversible": {"type": "boolean"},
                        "touches_pii": {"type": "boolean"}
                    },
                    "required": ["action_name", "monetary_value_usd", "is_reversible", "touches_pii"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "evaluate_hitl_approval_gate":
            args = params.get("arguments", {})
            res = HumanInTheLoopApprovalGate.evaluate_approval_gate(
                args.get("action_name", "action"),
                float(args.get("monetary_value_usd", 0.0)),
                bool(args.get("is_reversible", True)),
                bool(args.get("touches_pii", False))
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
