# curly-octo-rotary-phone

An ADK implementation of the [Thoughtful AI customer agent](https://thoughtfulautomation.notion.site/AI-Technical-Screen-d4d381a8c38d40fc9287cdb6c4f9992a)

# Setup

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Store it in the variable `GOOGLE_API_KEY` in the file `./customer_support/.env`

```bash
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate.bat on Windows
pip3 install -r requirements.txt
```

__NOTE__: With both outputs, they are verbose. Meaning, it will show the output of
each agent. We would show the user the output of the summary result as that is
the final agent.

## CLI

```bash
adk run customer_support
```

### Sample run

```bash
[user]: What do they do?
[RelevantQuestionAgent]: ```json
[
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    },
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
    }
]
```
[SummaryAgent]: Thoughtful AI offers AI automation agents like EVA, CAM, and PHIL to streamline healthcare processes, reduce costs, improve efficiency, and minimize errors in areas like eligibility verification, claims processing, and payment posting.
[user]: what does cam do?
[RelevantQuestionAgent]: ```json
[
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    }
]
```
[SummaryAgent]: CAM, the claims processing agent, streamlines claims submission and management, improving accuracy, reducing manual work, and speeding up reimbursements.

[user]: how about eav
[RelevantQuestionAgent]: ```json
[
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    }
]
```
[SummaryAgent]: EVA automates patient eligibility and benefits verification in real-time, cutting down on manual data entry errors and claim rejections.

[user]: and the other?
[RelevantQuestionAgent]: ```json
[
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    }
]
```
[SummaryAgent]: PHIL automates payment posting to patient accounts, ensuring quick and accurate reconciliation while reducing administrative work.
```

## Web

```bash
adk web
```
