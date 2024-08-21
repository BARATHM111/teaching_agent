import os
import anthropic
from prompts import *

# Set up the anthropic key
if not os.getenv("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = input("Please enter your API key: ")

# Create the anthropic client
client = anthropic.Anthropic()
sonnet = "claude-3-5-sonnet-20240620"

# Teaching agent to explain concepts
def teach_concept(concept):
    message = client.messages.create(
        model=sonnet,
        max_tokens=500,
        temperature=0.5,
        system=TEACHING_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": TEACHING_USER_PROMPT.format(concept=concept)
            }
        ]
    )
    return message.content[0].text

# Paper analysis agent
def analyze_paper(paper_content):
    message = client.messages.create(
        model=sonnet,
        max_tokens=1000,
        temperature=0.3,
        system=PAPER_ANALYSIS_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": PAPER_ANALYSIS_USER_PROMPT.format(paper_content=paper_content)
            }
        ]
    )
    return message.content[0].text
