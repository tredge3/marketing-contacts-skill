"""Marketing contacts skill for the sales AI assistant."""

from ..skill_model import SkillModel
from .tools import get_marketing_contacts


class MarketingContactsSkill(SkillModel):
    """Skill for accessing marketing contacts data from Snowflake."""

    subject = "Marketing Contacts"
    id = "marketing_contacts"
    routing_examples = (
        "marketing contacts",
        "marketing contacts for SAV ID {savm_id}",
        "get marketing contacts for SAV ID {savm_id}",
        "marketing contacts data for SAV ID {savm_id}",
        "get marketing contacts data for SAV ID {savm_id}",
        "marketing contacts for {savm_id}",
        "get marketing contacts for {savm_id}",
        "marketing contacts data for {savm_id}",
        "get marketing contacts data for {savm_id}",
        "Can you get marketing contacts data for SAV ID {savm_id}",
        "Can you get marketing contacts for SAV ID {savm_id}",
        "Can you get marketing contacts data for {savm_id}",
        "Can you get marketing contacts for {savm_id}",
        "3rd party marketing data contacts",
        "marketing data contacts",
        "get marketing data contacts",
        "marketing contacts from Snowflake",
        "Snowflake marketing contacts",
        "MKTG_DB marketing contacts",
        "SALES_AI_MKTG_CONTACTS",
        "marketing contacts table",
    )

    def __init__(self):
        """Initialize the marketing contacts skill."""
        self.tools = [get_marketing_contacts]
        self.description = "Access marketing contacts data from the MKTG_DB.MKTG_MOPS_BR.SALES_AI_MKTG_CONTACTS table"
