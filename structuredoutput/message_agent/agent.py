from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field


# --- Define Output Schema ---
class WhatsAppMessage(BaseModel):
    message: str = Field(
        description="""
        The WhatsApp message content.Keep it natural, concise, and conversational.Use plain text only.
        """
    )


# --- Create WhatsApp Generator Agent ---
root_agent = LlmAgent(
    name="whatsapp_agent",
    model="gemini-2.5-flash",
    instruction="""
        You are a WhatsApp Message Generation Assistant.

        Your task is to generate WhatsApp messages based on the user's request.

        GUIDELINES:
        - Keep messages short and conversational
        - Use a natural WhatsApp-style tone
        - Match the tone based on context:
            * Professional
            * Friendly
            * Casual
            * Apology
            * Follow-up
            * Reminder
        - Avoid long email-style formatting
        - Use plain text only
        - No markdown
        - No emojis unless user asks

        IMPORTANT:
        Your response MUST be valid JSON matching this structure:

        {
            "message": "Your WhatsApp message here"
        }

        DO NOT include explanations or extra text outside JSON.
    """,
    description="Generates WhatsApp messages in structured JSON format",
    output_schema=WhatsAppMessage,
    output_key="whatsapp_message",
)