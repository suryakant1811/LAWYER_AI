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
        "user_query": "Someone stole my OTP."
    },
    config=config
)

result2 = workflow2.invoke(
    {
        "user_query": result["user_query"],
        "intent_and_domain": result["intent_and_domain"],
        "user_answers": """
Name : Surya

State : Punjab

City : Jalandhar

Fraud Type : OTP Scam

Amount : ₹30,000

Platform : UPI

Transaction Date : Yesterday

Transaction ID : 987654321

Bank : SBI

FIR Filed : No

Evidence :
- SMS
- Screenshot
- Bank Statement
"""
    }
)

print(result2["final_response"])