# Marketing Contacts Skill for AIDE

A skill module for the AIDE (AI Development Environment) framework that provides access to marketing contacts data from Snowflake databases.

## 🎯 Purpose

This skill allows users to retrieve marketing contact information for specific SAVM IDs from the `MKTG_DB.MKTG_MOPS_BR.SALES_AI_MKTG_CONTACTS` table in Snowflake. It supports various SAV ID formats including `SAV_` and `GUC_` prefixes.

## 🚀 Features

- **Database Integration**: Connects to Snowflake using the AIDE framework's database connection utilities
- **Flexible ID Matching**: Supports multiple SAV ID formats (SAV_123456, GUC_123456_BRA, etc.)
- **Role-Based Access**: Implements customer-specific access permissions
- **Easy Integration**: Drop-in skill for existing AIDE chatbots

## 📁 Repository Structure

```
marketing-contacts-skill/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── src/
│   └── marketing_contacts/
│       ├── __init__.py          # Skill initialization
│       ├── tools.py             # Database tools and functions
│       └── skill.py             # Skill definition and routing
├── examples/
│   └── integration_example.py   # Usage examples
└── docs/
    └── integration_guide.md     # Detailed integration instructions
```

## 🛠️ Installation

### Prerequisites

- AIDE framework installed and configured
- Access to Snowflake database
- Proper environment variables set up

### Quick Start

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/marketing-contacts-skill.git
   cd marketing-contacts-skill
   ```

2. **Copy the skill to your AIDE chatbot:**
   ```bash
   cp -r src/marketing_contacts /path/to/your/aide/chatbot/src/skills/
   ```

3. **Add the skill to your chatbot configuration:**
   ```yaml
   # In your bot_config.yaml
   tools:
     - src.skills.marketing_contacts.tools.get_marketing_contacts
   ```

## 📖 Usage

### Basic Usage

Users can ask questions like:
- "Get marketing contacts for SAV ID 283631557"
- "Marketing contacts data for 329155077"
- "Can you retrieve marketing contacts for SAV ID 123456?"

### Supported SAV ID Formats

The skill automatically handles various ID formats:
- `SAV_283631557` (direct match)
- `GUC_329155077_BRA` (pattern matching)
- `283631557` (numeric search)

## 🔧 Configuration

### Environment Variables

Ensure these are set in your `.env` file:
```bash
SNOWFLAKE_DB_NAME_SCHEMA_NAME="ANALYTICS_DB.ANALYTICS_AI4SALES_BR"
# Other Snowflake credentials as needed
```

### Database Connection

The skill uses AIDE's `@with_db_connection()` decorator for database access:
```python
@with_db_connection()
def get_contacts_df(savm_id: str):
    # Database query logic
    return text(query), params
```

## 🧪 Testing

### Example Queries

1. **Basic contact retrieval:**
   ```
   "Get marketing contacts for SAV ID 283631557"
   ```

2. **Pattern matching:**
   ```
   "Marketing contacts for 329155077"
   ```

3. **General inquiries:**
   ```
   "Do you have access to 3rd party marketing data contacts?"
   ```

## 🔒 Security & Access Control

This skill implements role-based access control:
- Filters data based on user's CEC ID
- Uses customer access permissions
- Prevents unauthorized data access

## 🤝 Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the same terms as the AIDE framework.

## 🙏 Acknowledgments

- Built for the AIDE (AI Development Environment) framework
- Integrates with Cisco's Snowflake data infrastructure
- Follows AIDE skill development patterns and conventions

## 📞 Support

For questions or issues:
1. Check the [integration guide](docs/integration_guide.md)
2. Review the [examples](examples/)
3. Open an issue on this repository

---

**Note:** This skill is designed to work within the AIDE framework. For standalone usage, additional configuration may be required.
