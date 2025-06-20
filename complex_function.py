def decision(x: int) -> str:
    if x > 0:
        return "yes"
    elif x < 0:
        return "no"
    else:
        return "maybe"

# --- Agent Notes (linting / linting_generator_agent_provider) ---
# - Added type annotations to the `decision` function to specify that `x` is an `int` and the function returns a `str`, addressing the mypy violation.
# - Reformatted the code to conform to PEP8 standards using `black`, which involved adding spaces around operators and ensuring consistent indentation.
# - These changes improve code readability and maintainability without altering the original logic or structure.
# -----------------------------------------------
