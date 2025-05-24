from sklearn.cluster import KMeans
import numpy as np

def advanced_skin_tone(image):
    img = np.array(image.resize((100, 100)))
    img = img.reshape((-1, 3))
    kmeans = KMeans(n_clusters=3, random_state=0).fit(img)
    dominant_color = kmeans.cluster_centers_[0]
    r, g, b = dominant_color

    if r > 180 and g > 150 and b < 130:
        return "Warm"
    elif b > r and g > r:
        return "Cool"
    else:
        return "Neutral"
