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
        "user_query": "Someone get my phone number and took my otp and stole my 30,000 rupeess what to do now."
    },
    config=config
)

print(result["intent_and_domain"])

# print(result)

result2 = workflow2.invoke(
    {
         "user_query": result["user_query"],
         "intent_and_domain": result["intent_and_domain"],
         "user_answers": """
                State: Punjab
                No FIR
                No seizure receipt """
    }
)


print(result2["route"])
# print(result2["retrieved_context"])
print(result2)