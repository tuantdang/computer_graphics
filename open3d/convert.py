import open3d as o3d
import numpy as np

bunny = o3d.data.BunnyMesh()
mesh = o3d.io.read_triangle_mesh(bunny.path)
mesh.compute_vertex_normals()

pcl = mesh.sample_points_poisson_disk(number_of_points=2000)
# hull, _ = pcl.compute_convex_hull()
# hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
# hull_ls.paint_uniform_color((1, 0, 0))
points = np.asarray(pcl.points)
# o3d.visualization.draw_geometries([pcl])
np.save(f'data/bunny.npy', points)
