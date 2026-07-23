from workflow import workflow
from langchain_core.messages import HumanMessage
from workflow2 import workflow2

config = {
    "configurable": {
        "thread_id": "user-1"
    }
}
result = workflow.invoke(
    {
        "user_query": "Someone stole ₹30,000 using OTP fraud."
    },
    config=config
)

result2 = workflow2.invoke(
    {
        "user_query": result["user_query"],
        "intent_and_domain": result["intent_and_domain"],
        "user_answers": """
State: Punjab
No FIR
Transaction: UPI
"""
    }
)

print(result2["retrieved_context"])
print(result2["reasoning"])
print(result2["action_plan"])
print(result2["rights"])
print(result2["complaint_draft"])