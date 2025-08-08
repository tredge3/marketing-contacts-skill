"""
Example: How to use the Marketing Contacts Skill in AIDE

This example demonstrates how to integrate and use the marketing contacts skill
within an AIDE chatbot environment.
"""

# Example 1: Basic Integration
# Add this to your bot_config.yaml
bot_config_example = """
nodes:
  - name: default_agent
    type: agent
    tools:
      - src.skills.marketing_contacts.tools.get_marketing_contacts
"""

# Example 2: Assistant Configuration
# Add this to your src/assistant.py
assistant_config_example = """
from .skills.marketing_contacts import MarketingContactsSkill

SKILLS = (
    # ... existing skills ...
    MarketingContactsSkill(),
)
"""

# Example 3: User Queries
# These are examples of what users can ask:
user_queries = [
    "Get marketing contacts for SAV ID 283631557",
    "Marketing contacts data for 329155077",
    "Can you retrieve marketing contacts for SAV ID 123456?",
    "Do you have access to 3rd party marketing data contacts?",
    "Marketing contacts for SAV ID 283631557 please",
]

# Example 4: Expected Responses
expected_responses = [
    """
    Here are some marketing contacts for SAV ID 283631557 (JSW STEEL GROUP):

    1. Vijay Badiger - network admin - vijaym@bmm.in
    2. Santosh Yadawad - Assistant Manager - santosh.yadawad@jsw.in
    3. Ram Prasad - Head Security - grandhi.prasad@jsw.in
    ...
    """,
    
    """
    The contact information for SAV ID 329155077 (VISIONSET SEGURANCA EM TECNOLOGIA LTDA) is as follows:

    1. Eduardo Elias
       - Job Title: Sales Engineer
       - Email: eduardo.elias@asper.tec.br
       - Country: Brazil
    ...
    """
]

# Example 5: Testing the Skill
def test_marketing_contacts_skill():
    """
    Example function to test the marketing contacts skill
    """
    test_sav_ids = [
        "283631557",  # Should return JSW STEEL GROUP contacts
        "329155077",  # Should return VISIONSET contacts
        "999999999",  # Should return "No contacts found"
    ]
    
    for sav_id in test_sav_ids:
        print(f"Testing SAV ID: {sav_id}")
        # In a real AIDE environment, this would call the skill
        # result = get_marketing_contacts(sav_id)
        # print(f"Result: {result}")

# Example 6: Environment Variables
# Add these to your .env file
env_variables = """
# Snowflake Configuration
SNOWFLAKE_DB_NAME_SCHEMA_NAME="ANALYTICS_DB.ANALYTICS_AI4SALES_BR"

# User Configuration
USER_ID="your_user_id"

# Optional: Debug logging
LOG_LEVEL="DEBUG"
"""

# Example 7: Custom Query Modification
# If you want to modify the database query, edit src/marketing_contacts/tools.py:
custom_query_example = """
@with_db_connection()
def get_contacts_df(savm_id: str):
    # Custom query with additional filters
    query = '''
    SELECT 
        UUID,
        FIRST_NAME,
        LAST_NAME,
        EMAIL_ADDRESS,
        JOB_TITLE,
        SAVM_ACCOUNT_OR_COMPANY_NAME,
        ISO_COUNTRY_NAME
    FROM MKTG_DB.MKTG_MOPS_BR.SALES_AI_MKTG_CONTACTS
    WHERE SAVM_ACCOUNT_OR_COMPANY_ID = :savm_id_sav
       OR SAVM_ACCOUNT_OR_COMPANY_ID LIKE :savm_id_guc_pattern
    AND EMAIL_ADDRESS IS NOT NULL
    ORDER BY FIRST_NAME, LAST_NAME
    LIMIT 20
    '''
    
    params = {
        "savm_id_sav": f"SAV_{savm_id}",
        "savm_id_guc_pattern": f"GUC_{savm_id}_%"
    }
    
    return text(query), params
"""

if __name__ == "__main__":
    print("Marketing Contacts Skill Integration Examples")
    print("=" * 50)
    print("\n1. Bot Configuration:")
    print(bot_config_example)
    print("\n2. Assistant Configuration:")
    print(assistant_config_example)
    print("\n3. Example User Queries:")
    for i, query in enumerate(user_queries, 1):
        print(f"   {i}. {query}")
    print("\n4. Environment Variables:")
    print(env_variables)
