"""Marketing contacts tools for the sales AI assistant."""

from langchain_core.tools import tool
from sqlalchemy import text

from ...db import with_db_connection


@tool
def get_marketing_contacts(savm_id: str) -> str:
    """
    Get marketing contacts data from Snowflake for a specific SAVM ID.
    
    Args:
        savm_id: SAVM ID to search for (e.g., "283631557")
    
    Returns:
        str: Marketing contacts data or error message
    """
    try:
        # Get the data using the decorator
        result = get_contacts_df(savm_id)
        
        if result.empty:
            return f"No marketing contacts found for SAVM ID: {savm_id}"
        
        # Convert to string for simple display
        return f"Found marketing contacts: {result.to_dict('records')}"
        
    except Exception as e:
        return f"Error retrieving marketing contacts: {str(e)}"


@with_db_connection()
def get_contacts_df(savm_id: str):
    """Get marketing contacts data for a SAVM ID.
    
    Args:
        savm_id: SAVM ID to search for
        
    Returns:
        tuple: (SQLAlchemy statement, params dict) for execution by decorator
    """
    # Query to get marketing contacts
    query = """
    SELECT * FROM MKTG_DB.MKTG_MOPS_BR.SALES_AI_MKTG_CONTACTS 
    WHERE SAVM_ACCOUNT_OR_COMPANY_ID = :savm_id_sav
       OR SAVM_ACCOUNT_OR_COMPANY_ID LIKE :savm_id_guc_pattern
    LIMIT 10
    """
    
    params = {
        "savm_id_sav": f"SAV_{savm_id}",
        "savm_id_guc_pattern": f"GUC_{savm_id}_%"
    }
    
    return text(query), params
