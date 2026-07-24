# JusticeFlow

JusticeFlow is a legal-first AI assistant built to help users understand their rights, identify the relevant domain, gather missing case details, retrieve grounded legal knowledge, and generate a structured response for civil, consumer, cybercrime, employment, and other public-rights-related issues.

This project was designed as a professional AI-powered legal guidance workflow that combines:

- Large language model reasoning
- Domain routing
- Retrieval-augmented generation (RAG)
- Multi-step legal workflow orchestration
- Structured complaint and rights drafting support

The goal is not to replace a lawyer, but to help a user move from a vague problem statement to a clearer understanding of:

- what issue they are facing,
- which legal domain it belongs to,
- what facts are still missing,
- what rights and remedies may apply,
- and how to frame a formal complaint or next step.

---

## What I Built

This project implements a multi-agent, multi-stage conversational legal assistant using LangGraph and LangChain.

The system works in two major phases:

1. Intake and clarification phase
   - Understand the user’s problem
   - Identify intent and domain
   - Ask only the most relevant follow-up questions

2. Legal reasoning and response generation phase
   - Route the case to the correct legal domain
   - Retrieve relevant legal knowledge from a vector database
   - Reason over that context
   - Create an action plan
   - Extract rights and remedies
   - Draft a complaint-oriented response
   - Produce a final structured answer

---

## Why This Project Exists

Millions of people face legal and civic issues without knowing:

- which law applies,
- which authority to contact,
- what evidence is needed,
- or whether their issue is a consumer, cybercrime, police, employment, or healthcare matter.

JusticeFlow tries to reduce that confusion by turning a natural-language problem into a guided legal workflow.

---

## High-Level Architecture

The project is organized into three main layers:

### 1. Workflow Orchestration
The workflow layer coordinates the entire reasoning pipeline.

- `Agent/workflow.py` = first-stage workflow
- `Agent/workflow2.py` = second-stage workflow

These workflows use LangGraph state graphs where each node updates shared state and passes control to the next step.

### 2. AI Nodes
Each node is responsible for one step in the legal reasoning chain.

- `intent_node.py` identifies the user’s intent and domain
- `question_node.py` decides what missing facts are essential
- `router_node.py` selects the most relevant route
- `retriever_node.py` retrieves context from the vector database
- `reasoning_node.py` interprets the retrieved information
- `planner_node.py` creates an action plan
- `rights_node.py` extracts rights and legal remedies
- `complaint_node.py` frames the complaint or escalation path
- `final_node.py` generates the final user-facing answer

### 3. Knowledge and Retrieval Layer
The knowledge layer stores legal knowledge documents and turns them into searchable vector embeddings.

- `RAG/loader.py` loads source documents
- `RAG/splitter.py` splits documents into chunks
- `RAG/embeddings.py` builds embeddings
- `RAG/vectorstore.py` creates the vector DB
- `RAG/retrieve.py` searches for relevant context at runtime

---

## How the Flow Works

### Stage 1: Problem Intake
The user starts with a plain-language query such as:

> “Someone stole my OTP and my bank account was drained.”

The first workflow receives this input and performs intent classification.

### Stage 2: Information Collection
The system determines whether enough facts are available to proceed.

It asks questions such as:

- State and city
- What happened
- Amount involved
- Platform or bank involved
- Date of occurrence
- Evidence available
- Whether an FIR has been filed

This is important because legal guidance becomes more useful when the facts are concrete and complete.

### Stage 3: Routing
After the user answer is captured, the router chooses the most relevant domain route, such as:

- banking
- police
- consumer
- cybercrime
- employment
- property
- education
- healthcare
- general

### Stage 4: Retrieval-Augmented Legal Context
The retriever searches the vector database for related legal material and returns context chunks from the relevant domain documents.

This means the later reasoning is grounded in legal knowledge instead of depending purely on the model’s general memory.

### Stage 5: Reasoning and Planning
The AI reasoning node interprets the retrieved context and builds a structured understanding of the issue.

The planner then creates an action plan describing what the user should do next.

### Stage 6: Rights and Complaint Drafting
The system then derives:

- applicable rights,
- likely remedies,
- relevant authority or action path,
- and a complaint template or escalation direction.

### Stage 7: Final Response
The final node combines all previous outputs into a coherent answer that is meant to be practical, structured, and easy to understand.

---

## What “Strict” Means in This Project

When I say the project is “strict,” I mean that the workflow is intentionally structured and constrained rather than loose and open-ended.

In practice, that means:

- the agent follows a defined sequence of steps,
- every major stage updates shared state,
- the response is built from a consistent legal pipeline,
- routing is domain-based instead of random,
- retrieval is used to ground the answer in documents,
- and the output is assembled from clearly separated reasoning stages.

So the “strictness” is not about being rigid in the wrong way. It is a disciplined design principle:

- clear inputs,
- clear nodes,
- clear state transitions,
- clear grounding in legal knowledge,
- and a final response derived from a reproducible workflow.

This makes the system more explainable, more maintainable, and easier to improve over time.

---

## Project Structure

```text
JusticeFlow/
├── Agent/
│   ├── main.py
│   ├── workflow.py
│   ├── workflow2.py
│   ├── model.py
│   ├── state/
│   ├── nodes/
│   ├── prompts/
│   ├── RAG/
│   └── documents/
├── infra/
└── README.md
```

### Main folders

- `Agent/` — the core application and legal workflow engine
- `Agent/nodes/` — individual LangGraph nodes
- `Agent/prompts/` — prompt templates for each stage
- `Agent/RAG/` — retrieval, embedding, chunking, and vector store logic
- `Agent/documents/` — domain knowledge resources for multiple legal categories
- `infra/` — deployment related assets

---

## Tech Stack

This project is built using:

- Python
- LangChain
- LangGraph
- Chroma vector database
- Groq / LLM model integration via `init_chat_model`
- Retrieval-augmented generation pipeline

---

## Environment Setup

1. Create a virtual environment
2. Install dependencies
3. Add your API keys in a `.env` file
4. Make sure the vector database is initialized

Example environment variables:

```env
GROQ_API_KEY_BACKUP=your_key_here
```

---

## Run the Project

From the workspace root:

```bash
cd Agent
python main.py
```

This will invoke the workflow with a sample user query and print the final legal response.

---

## Data and Knowledge Base

The knowledge layer is domain-specific and includes content for areas such as:

- banking
- consumer protection
- cybercrime
- education
- employment
- healthcare
- police
- property

These documents are stored in markdown files and later indexed into a vector database for retrieval.

---

## Important Design Notes

### Why LangGraph?
LangGraph gives the system a graph-based workflow where each node has a clear function and the conversation state is shared across steps.

This makes the workflow:

- modular,
- easier to debug,
- better for controlled reasoning,
- and easier to extend with more legal nodes later.

### Why RAG?
Typical LLMs can give generic answers. RAG allows the assistant to pull evidence from legal source files, which helps make the response more grounded and document-aware.

### Why a Multi-Stage Pipeline?
A single prompt is often too broad. This workflow separates:

- understanding,
- missing fact collection,
- routing,
- retrieval,
- reasoning,
- action planning,
- and final synthesis.

That split improves structure and makes the system easier to improve.

---

## Current Status

This project is a strong prototype / production-style proof of concept for an AI legal guidance platform.

It already demonstrates:

- intent and route detection,
- guided question generation,
- retrieval from a legal knowledge base,
- multi-step legal reasoning,
- rights and complaint generation,
- and a final user response pipeline.

---

## Future Improvements

Potential next steps for this project include:

- adding a web interface
- adding authentication and user sessions
- improving domain-specific validation
- adding better citation and source traceability
- creating a safer legal compliance layer
- adding vector DB refresh automation
- integrating a frontend dashboard for complaint drafting

---

## Summary

JusticeFlow is a structured AI legal assistant that transforms a user’s complaint into a disciplined legal workflow.

It combines:

- conversational intake,
- domain routing,
- document retrieval,
- LLM reasoning,
- rights extraction,
- and complaint-oriented answer generation.

The core idea behind the system is simple and professional:

> Build a legal assistance tool that is explainable, grounded in documents, and strict in its workflow design.
