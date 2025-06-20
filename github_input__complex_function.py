def decision(x: int) -> str:
    if x > 0:
        return 'yes'
    elif x < 0:
        return 'no'
    else:
        return 'maybe'

# --- Agent Notes (linting / linting_generator_agent_provider) ---
# - Added type annotations to the `decision` function to specify that it takes an integer `x` and returns a string. This resolves the mypy violation regarding missing type annotations.
# - Reformatted the code to comply with PEP8 guidelines, specifically by adding indentation and line breaks for better readability. This addresses the black violation about reformatting.
# - Preserved the original logic and structure of the function to maintain its intended behavior.
# -----------------------------------------------
