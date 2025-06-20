def decision(x: int) -> str:
    if x > 0:
        return "yes"
    elif x < 0:
        return "no"
    else:
        return "maybe"

# --- Agent Notes (linting / linting_generator_agent_provider) ---
# - Added type annotations to the `decision` function to specify that it takes an integer and returns a string. This resolves the mypy violation regarding missing type annotations.
# - Reformatted the code to conform to PEP8 standards using `black`, which involved adding indentation and spacing for better readability.
# - Ensured that the original logic and structure of the function were preserved while making these improvements.
# -----------------------------------------------
