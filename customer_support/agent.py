from google.adk.agents import LlmAgent, SequentialAgent

relevant_question_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="RelevantQuestionAgent",
    description="Returns relevant questions/answer pairs for the given context",
    instruction="""
Given the following questions and answers along with the context, return an array of the most relevant questions and answers. If none are relevant, then return an empty array.

```json
{
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}
```
    """,
)

summary_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="SummaryAgent",
    description="Summarize question/answer pairs as something human readable",
    instruction="""
Summarize the question/answer pair as an answer to the user's question.
""",
)

# ADK offers only a few agent types to form a directed acyclic graph (DAG). The
# DAG has to have a root_agent to start.
#
# We'll use the following agent types:
# * LlmAgent - Passes instructions to a LLM to allow it to either chose from it's sub_agents or ask
#   the user a followup question (multi-turn). If it chooses to ask the user a question, LlmAgent is
#   invoked after the user responds and the DAG .
# * SequentialAgent - Always invoke each sub-agent in order.
#
# So we'll create a very simple DAG where we first pass the session to an LlmAgent where we have it
# choose the relevant question/answer pairs. We'll then pass that output to a
# different LlmAgent that summarizes the pairs in a way that makes sense for
# the session context. We'll orchestrate the ordering with a SequentialPair.
#
# I chose this design as I wanted to ensure the user's question is grounded
# with the most relevant data and then summarized in a way to ensure it answers
# the question (as opposed to responding with an answer directly from the
# sample data). I wanted each agent to have a minimal job (e.g., pick question/answer pairs,
# summarize question/answer pairs) so that if additional features were later needed, we could simply
# add to the DAG without having to rethink each agent.

root_agent = SequentialAgent(
        name="root_agent",
        sub_agents=[relevant_question_agent, summary_agent]
)


# If you want to get real fancy, we can deploy it to AgentEngine
#
# import vertexai
#
# PROJECT_ID = "your-project-id"
# LOCATION = "us-central1"
# STAGING_BUCKET = "gs://your-google-cloud-storage-bucket"
#
# vertexai.init(
#     project=PROJECT_ID,
#     location=LOCATION,
#     staging_bucket=STAGING_BUCKET,
# )
