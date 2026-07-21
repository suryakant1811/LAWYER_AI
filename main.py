from workflow import workflow
from langchain_core.messages import HumanMessage

config = {
    "configurable": {
        "thread_id": "user-1"
    }
}

result = workflow.invoke(
    {
        "user_query": [
            HumanMessage(content="SBI refused to open my account.")
        ]
    },
    config=config
)



print(result)