"""Marketing contacts skill for the sales AI assistant.

## Purpose

Access marketing contacts data from the MKTG_DB.MKTG_MOPS_BR.SALES_AI_MKTG_CONTACTS table in Snowflake.
This skill allows users to retrieve marketing contact information for specific SAVM IDs.

## Example questions

- Marketing contacts for SAV ID 283631557
- Get marketing contacts data for SAV ID 283631557
- Marketing contacts for 283631557
- Get marketing contacts for 283631557
- 3rd party marketing data contacts
- Marketing data contacts for SAV ID 283631557
- Snowflake marketing contacts
- MKTG_DB marketing contacts
"""

from .marketing_contacts_skill import MarketingContactsSkill

__all__ = ["MarketingContactsSkill"]
