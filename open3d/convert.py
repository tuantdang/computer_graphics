import open3d as o3d
import numpy as np

bunny = o3d.data.BunnyMesh()
mesh = o3d.io.read_triangle_mesh(bunny.path)
mesh.compute_vertex_normals()

pcl = mesh.sample_points_poisson_disk(number_of_points=2000)
# hull, _ = pcl.compute_convex_hull()
# hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
# hull_ls.paint_uniform_color((1, 0, 0))
# points = np.asarray(pcl.points)
# o3d.visualization.draw_geometries([mesh])
# np.save(f'data/bunny.npy', points)
# o3d.io.write_triangle_mesh(f'data/bunny.stl', mesh)
# Apply vertex clustering
mesh = mesh.simplify_vertex_clustering(voxel_size=0.02)
vertices = np.asanyarray(mesh.vertices) 
triangles = np.asanyarray(mesh.triangles)
normals = np.asanyarray(mesh.triangle_normals)

# o3d.visualization.draw_geometries([mesh])
# print(len(vertices))
# print(len(triangles))
# print(len(normals))
# print(normals[0:5])
n = len(triangles)
with open(f'data/bunny.stl', "w") as file:
    file.write("solid bunny\n")
    for i in range(n): # each triangle
        normal = normals[i]
        triangle = triangles[i]
        v1 = vertices[triangle[0]]
        v2 = vertices[triangle[1]]
        v3 = vertices[triangle[2]]
        file.write(f'  face normal {normal[0]} {normal[1]} {normal[2]}\n')
        file.write(f'    outer loop\n')
        for j in range(3):
            v = vertices[triangle[j]]
            file.write(f'      vertex {v[0]} {v[1]} {v[2]}\n')
        file.write(f'    endloop\n')
        file.write(f'  endfacet\n')
    file.write("endsolid bunny")     
