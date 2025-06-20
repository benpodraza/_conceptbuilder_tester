def decision(x: int) -> str:
    if x > 0:
        return 'yes'
    elif x < 0:
        return 'no'
    else:
        return 'maybe'

# --- Agent Notes (linting / linting_generator_agent_provider) ---
# - Added type annotations to the function `decision` to specify that it takes an integer `x` and returns a string. This resolves the mypy violation about missing type annotations.
# - Reformatted the code to comply with PEP8 guidelines using `black`, which involved adding proper indentation and spacing around operators and keywords.
# - These changes improve code readability and maintainability without altering the original logic or structure.
# -----------------------------------------------
