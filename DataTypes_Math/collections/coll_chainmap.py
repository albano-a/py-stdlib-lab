from collections import ChainMap

# Nested scopes
defaults = {"theme": "light", "language": "en", "timeout": 30}
user_config = {"language": "pt"}
session_config = {"timeout": 10, "theme": "dark"}

# search order: sessions -> user -> defaults
config = ChainMap(session_config, user_config, defaults)

# Lookup: searches in order and returns first match
print("Theme:", config["theme"])            # from session_config
print("Language:", config["language"])      # from user_config
print("Timeout:", config["timeout"])        # from session_config

# Update: only affects first mapping
config['theme'] = 'solarized'
print("Session config after update:", session_config)
