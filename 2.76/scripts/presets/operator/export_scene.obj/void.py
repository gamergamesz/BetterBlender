import bpy
op = bpy.context.active_operator

op.filepath = 'E:\\3D\\blender\\Dyntopo\\Jam 2014 06 06\\OBJ\\05_sweater_blend.obj'
op.use_selection = True
op.use_animation = False
op.use_mesh_modifiers = True
op.use_edges = True
op.use_smooth_groups = False
op.use_smooth_groups_bitflags = False
op.use_normals = False
op.use_uvs = True
op.use_materials = True
op.use_triangles = False
op.use_nurbs = False
op.use_vertex_groups = False
op.use_blen_objects = True
op.group_by_object = False
op.group_by_material = False
op.keep_vertex_order = True
op.axis_forward = '-Z'
op.axis_up = 'Y'
op.global_scale = 1.0
op.path_mode = 'AUTO'
