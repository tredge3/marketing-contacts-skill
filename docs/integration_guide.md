# Integration Guide: Marketing Contacts Skill for AIDE

This guide explains how to integrate the Marketing Contacts Skill into your AIDE chatbot.

## Prerequisites

- AIDE framework installed and running
- Access to Snowflake database
- Proper environment variables configured

## Step-by-Step Integration

### 1. Copy Skill Files

Copy the marketing contacts skill to your chatbot's skills directory:

```bash
# From your AIDE chatbot directory
cp -r /path/to/marketing-contacts-skill/src/marketing_contacts \
      chatbots/your_bot_name/src/skills/
```

### 2. Update Assistant Configuration

Add the skill to your assistant's skill list in `src/assistant.py`:

```python
# Add this import at the top
from .skills.marketing_contacts import MarketingContactsSkill

# Add to the SKILLS tuple
SKILLS = (
    # ... existing skills ...
    MarketingContactsSkill(),
)
```

### 3. Update Bot Configuration

Add the tool to your `bot_config.yaml`:

```yaml
nodes:
  - name: default_agent
    type: agent
    tools:
      # ... existing tools ...
      - src.skills.marketing_contacts.tools.get_marketing_contacts
```

### 4. Environment Variables

Ensure these are set in your `.env` file:

```bash
# User configuration
USER_ID="your_user_id"
```

### 5. Test the Integration

Restart your AIDE chatbot and test with:

```
"Get marketing contacts for SAV ID 283631557"
```

## Configuration Options

### Customizing the Query

You can modify the database query in `src/marketing_contacts/tools.py`:

```python
@with_db_connection()
def get_contacts_df(savm_id: str):
    query = """
    SELECT * FROM MKTG_DB.MKTG_MOPS_BR.SALES_AI_MKTG_CONTACTS
    WHERE SAVM_ACCOUNT_OR_COMPANY_ID = :savm_id_sav
       OR SAVM_ACCOUNT_OR_COMPANY_ID LIKE :savm_id_guc_pattern
    LIMIT 10
    """
    # ... rest of function
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure the skill is in the correct directory structure
   - Check that `__init__.py` files are present

2. **Database Connection Issues**
   - Verify Snowflake credentials in `.env`
   - Check network connectivity to Snowflake

3. **Tool Not Found**
   - Ensure the tool is added to `bot_config.yaml`
   - Restart the AIDE backend after configuration changes

### Debug Mode

Enable debug logging in your AIDE configuration:

```yaml
env:
  LOG_LEVEL: "DEBUG"
```

## Advanced Configuration

### Custom Routing Examples

Modify routing examples in `src/marketing_contacts/skill.py`:

```python
routing_examples = (
    "marketing contacts",
    "marketing contacts for SAV ID {savm_id}",
    # Add your custom patterns here
    "get contact info for {savm_id}",
)
```

### Multiple Database Support

To support multiple databases, modify the `@with_db_connection()` decorator:

```python
@with_db_connection(database="MARKETING_DB", env="PROD")
def get_contacts_df(savm_id: str):
    # ... function implementation
```

## Best Practices

1. **Always test** with sample SAV IDs before deployment
2. **Implement proper error handling** for database failures
3. **Monitor query performance** for large datasets
4. **Document any customizations** for team members

## Support

For additional help:
- Check the [AIDE documentation](https://github.com/Cisco-DES/aide)
- Review the [examples](../examples/) directory
- Open an issue on this repository
