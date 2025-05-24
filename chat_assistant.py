def assistant_reply(user_input):
    user_input = user_input.lower()

    if "foundation" in user_input:
        return "Choose a foundation that matches your undertone. For dry skin, use liquid-based products."
    elif "lipstick" in user_input:
        return "Matte lipsticks are great for a bold look. Try warm shades like coral or peach for warm tones."
    elif "eyes" in user_input:
        return "Neutral eyeshadow shades suit most tones. Add shimmer for special occasions."
    elif "skin care" in user_input or "routine" in user_input:
        return "Cleanse, tone, and moisturize daily. Use SPF even indoors."
    else:
        return "Ask me about foundations, lipsticks, eye makeup, or skincare!"
