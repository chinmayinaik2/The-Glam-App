import numpy as np

def detect_skin_tone(image):
    img = np.array(image)
    avg_color = img.reshape(-1, 3).mean(axis=0)
    r, g, b = avg_color

    if r > 180 and g > 150 and b < 130:
        return "Warm"
    elif b > r and g > r:
        return "Cool"
    else:
        return "Neutral"
