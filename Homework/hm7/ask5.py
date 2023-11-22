import numpy as np

def random_point_on_sphere(radius):
    """Generate a random point on the surface of a sphere."""
    phi = np.random.uniform(0, np.pi * 2)  # Random longitude
    theta = np.arccos(np.random.uniform(-1, 1))  # Random latitude
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    return x, y, z

def latitude_from_point(x, y, z, radius):
    """Calculate the latitude from a point on the sphere."""
    lat = np.arcsin(z / radius)  # Latitude in radians
    lat_deg = np.degrees(lat)  # Convert to degrees
    return lat_deg

def latitude_zone(latitude):
    """Determine the latitude zone for a given latitude."""
    if latitude >= 0:
        return int(latitude // 10) + 1  # Zone 1 to 9 for northern hemisphere
    else:
        return 0  # Southern hemisphere, not part of the 9 zones

# Monte Carlo simulation parameters
radius = 6400  # Earth's radius in km
num_attempts = 10**6
zone_counts = np.zeros(10)  # 9 zones plus one extra for southern hemisphere

# Perform the Monte Carlo simulation
for _ in range(num_attempts):
    x, y, z = random_point_on_sphere(radius)
    lat = latitude_from_point(x, y, z, radius)
    zone = latitude_zone(lat)
    zone_counts[zone] += 1

# Calculate the percentage of the surface area for each zone
zone_percentages = (zone_counts / num_attempts) * 100

# Display the results
zone_percentages[1:]  # Exclude the southern hemisphere (zone 0)

print(zone_percentages)
