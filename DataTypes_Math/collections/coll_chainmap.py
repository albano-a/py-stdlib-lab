"""
ChainMap groups multiple dictionaries (or mappings) into a single, unified view.
It enables:
- Efficient layered config or scope resolution (e.g., session -> user -> defaults)
- Updates and deletions that only affect the first mapping
- Read-through behavior across all mappings
- Temporary overrides using new_child()
- Scope traversal using .parents

This is useful in config systems, templating engines, interpreters, or any case
where nested environments need to be simulated without merging dictionaries.
"""

from collections import ChainMap

# Nested scopes
defaults = {"theme": "light", "language": "en", "timeout": 30}
user_config = {"language": "pt"}
session_config = {"timeout": 10, "theme": "dark"}

# search order: sessions -> user -> defaults
config = ChainMap(session_config, user_config, defaults)

# Lookup: searches in order and returns first match
print("Theme:", config["theme"])  # from session_config
print("Language:", config["language"])  # from user_config
print("Timeout:", config["timeout"])  # from session_config

# Update: only affects first mapping
config["theme"] = "solarized"
print("Session config after update:", session_config)

# Only removes from first mapping
del config["timeout"]
print("Timeout after delete:", config.get("timeout"))  # Now from defaults

print("All maps:", config.maps)

# Add a temporary child context (e.g., inside a function)
temp_config = config.new_child({"debug": True})
print("Debug mode:", temp_config["debug"])  # from new top mapping

# Revert to parent context
print(
    "Without temporary layer:",
    temp_config.parents["debug"] if "debug" in temp_config.parents else "not set",
)

# Demonstrate update by reference
user_config["language"] = "es"
print("Updated language via ChainMap:", config["language"])

# Iteration order (like update order)
print("Keys in ChainMap:", list(config))
