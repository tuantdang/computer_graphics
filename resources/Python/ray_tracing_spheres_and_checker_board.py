from PIL import Image
import numpy as np
import time
import numbers
import functools


def extract_elements(condition, x):
    if isinstance(x, numbers.Number):
        return x
    else:
        return np.extract(condition, x)
class clPoint3d():
    def __init__(self, x, y, z):
        (self.x, self.y, self.z) = (x, y, z)
    def __sub__(self, other_point):
        return clVector3d(self.x - other_point.x, self.y - other_point.y, self.z - other_point.z)

    def get_components(self):
        return (self.x, self.y, self.z)
    def extract_elements(self, condition):
        return clVector3d(extract_elements(condition, self.x),
                          extract_elements(condition, self.y),
                          extract_elements(condition, self.z))
    def replace_elements(self, condition):
        temp = clVector3d(np.zeros(condition.shape), np.zeros(condition.shape), np.zeros(condition.shape))
        np.place(temp.x, condition, self.x)
        np.place(temp.y, condition, self.y)
        np.place(temp.z, condition, self.z)
        return temp

class clVector3d():
    def __init__(self, x, y, z):
        (self.x, self.y, self.z) = (x, y, z)
    def __mul__(self, other_vector):
        return clVector3d(self.x * other_vector, self.y * other_vector, self.z * other_vector)
    def __add__(self, other_vector):
        return clVector3d(self.x + other_vector.x, self.y + other_vector.y, self.z + other_vector.z)
    def __sub__(self, other_vector):
        return clVector3d(self.x - other_vector.x, self.y - other_vector.y, self.z - other_vector.z)
    def dot(self, other_vector):
        return (self.x * other_vector.x) + (self.y * other_vector.y) + (self.z * other_vector.z)
    def mag(self):
        return np.linalg.norm(self)
    def normalize(self):
        magnitude = np.sqrt(self.dot(self))
        return self * (1.0 / np.where(magnitude == 0, 1, magnitude))
    def get_components(self):
        return (self.x, self.y, self.z)
    def extract_elements(self, condition):
        return clVector3d(extract_elements(condition, self.x),
                          extract_elements(condition, self.y),
                          extract_elements(condition, self.z))
    def replace_elements(self, condition):
        temp = clVector3d(np.zeros(condition.shape), np.zeros(condition.shape), np.zeros(condition.shape))
        np.place(temp.x, condition, self.x)
        np.place(temp.y, condition, self.y)
        np.place(temp.z, condition, self.z)
        return temp


def raytrace(ray_starting_point, normalized_ray_direction, objects_list, number_of_bounces = 1):
    intersections=[]
    for current_object in objects_list:
        intersections.append(current_object.intersect(ray_starting_point, normalized_ray_direction))
    # intersections= [object.intersect(ray_starting_point, normalized_ray_direction) for object in objects_list]
    nearest=[]

    nearest = functools.reduce(np.minimum, intersections)
    color = rgb(0, 0, 0)
    for (object, intersection) in zip(objects_list, intersections):
        hit = (nearest != infinity_plus) & (intersection == nearest)
        if np.any(hit):
            dc = extract_elements(hit, intersection)
            Oc = ray_starting_point.extract_elements(hit)
            Dc = normalized_ray_direction.extract_elements(hit)
            cc = object.light(Oc, Dc, dc, objects_list, number_of_bounces)
            color += cc.replace_elements(hit)
    return color

class Sphere:
    def __init__(self, center, radius, diffuse, specular_coef = 0.5):
        self.center = center
        self.radius = radius
        self.diffuse = diffuse
        self.specular_coef = specular_coef

    def intersect(self, ray_starting_point, normalized_ray_direction):
        eye_to_center=ray_starting_point - self.center
        b = 2 * normalized_ray_direction.dot(eye_to_center)
        c = eye_to_center.dot(eye_to_center) - (self.radius * self.radius)
        discriminant = (b ** 2) - (4 * c)
        discriminant_root = np.sqrt(np.maximum(0, discriminant))
        root1 = (-b - discriminant_root) / 2.0
        root2 = (-b + discriminant_root) / 2.0
        selected_root = np.where((root1 > 0) & (root1 < root2), root1, root2)
        # pred = (discriminant > 0) & (selected_root > 0)
        return np.where((discriminant > 0) & (selected_root > 0), selected_root, infinity_plus)

    def diffusecolor(self, M):
        return self.diffuse

    def light(self, ray_starting_point, normalized_ray_direction, intersection, objects_list, number_of_bounces):
        M = (ray_starting_point + normalized_ray_direction * intersection)                         # intersection point
        N = (M - self.center) * (1. / self.radius)        # normal
        toL = (light_position - M).normalize()                    # direction to light
        toO = (eye_position - M).normalize()                    # direction to ray origin
        nudged = M + N * .0001                  # M nudged to avoid itself

        # Shadow: find if the point is shadowed or not.
        # This amounts to finding out if M can see the light
        light_distances = [object.intersect(nudged, toL) for object in objects_list]
        light_nearest = functools.reduce(np.minimum, light_distances)
        seelight = light_distances[objects_list.index(self)] == light_nearest

        # Ambient
        color = rgb(0.05, 0.05, 0.05)

        # Lambert shading (diffuse)
        lv = np.maximum(N.dot(toL), 0)
        color += self.diffusecolor(M) * lv * seelight

        # Reflection
        if number_of_bounces < 5:
            rayD = (normalized_ray_direction - N * 2 * normalized_ray_direction.dot(N)).normalize()
            color += raytrace(nudged, rayD, objects_list, number_of_bounces + 1) * self.specular_coef

        # Blinn-Phong shading (specular)
        phong = N.dot((toL + toO).normalize())
        color += rgb(1, 1, 1) * np.power(np.clip(phong, 0, 1), 50) * seelight
        return color

class CheckeredSphere(Sphere):
    def diffusecolor(self, M):
        checker = ((M.x * 2).astype(int) % 2) == ((M.z * 2).astype(int) % 2)
        return self.diffuse * checker
rgb = clVector3d

(screen_width, screen_height) = (1200, 800)         # Screen size
light_position = clPoint3d(5, 5., -10)        # Point light position
eye_position = clPoint3d(5., 1.10, -10.)     # Eye position
infinity_plus = 1.0e39            # an implausibly huge distance
objects_list = [
    Sphere(clPoint3d(0.0, 0.0, 0.0), 0.1, rgb(1, 0, 0)),
    Sphere(clPoint3d(0.0, 0.10, 0.0), 0.1, rgb(0, 1, 0)),
    Sphere(clPoint3d(0.0, 0.0, 1.0), 0.1, rgb(1, 1, 0)),
    Sphere(clPoint3d(0.0, 0.4, 1.0), .1, rgb(.5, .223, .5)),
    CheckeredSphere(clPoint3d(0,-99999.5, 0), 99999, rgb(.75, .75, .75), 0.7),
    ]

screen_ratio = float(screen_width) / screen_height
# Screen coordinates: x0, y0, x1, y1.
screen_corners = (-1., 1. / screen_ratio + .25, 1., -1. / screen_ratio + .25)
x = np.tile(np.linspace(screen_corners[0], screen_corners[2], screen_width), screen_height)
y = np.repeat(np.linspace(screen_corners[1], screen_corners[3], screen_height), screen_width)

pixel_coordinates = clPoint3d(x, y, 0)
color = raytrace(eye_position, (pixel_coordinates - eye_position).normalize(), objects_list)
rgb = [Image.fromarray((255 * np.clip(c, 0, 1).reshape((screen_height, screen_width))).astype(np.uint8), "L") for c in color.get_components()]
Image.merge("RGB", rgb).show()
# Image.merge("RGB", rgb).save("fig.png")
