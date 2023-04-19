import bpy
import requests
import json

from bpy.types import Operator 


class CUSTOM_OT_Post_Operator(Operator):
    bl_idname = "object.post_to_server"
    bl_label = "Post"
    bl_description = "Post the model to the server"

    # defines if the operator should be enabled
    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True

        return False

    def execute(self,context):
        # do something
        name = "test"
        path = 'D:/0_Synology_Zan/07_faks/3.Letnik/Diplomska/DUMP'

        filePath = path + name

        bpy.ops.export_scene.gltf(filepath=filePath, # might change
                                  check_existing=True, 
                                  #convert_lighting_mode='SPEC', 
                                  export_format='GLTF_EMBEDDED', # might change
                                  ui_tab='GENERAL', 
                                  export_copyright=filePath, 
                                  export_image_format='AUTO', # might change
                                  export_texture_dir=filePath, # might change
                                  export_keep_originals=False, # might change
                                  export_texcoords=True, 
                                  export_normals=True, 
                                  export_draco_mesh_compression_enable=False, # might change
                                  export_draco_mesh_compression_level=6, 
                                  export_draco_position_quantization=14, 
                                  export_draco_normal_quantization=10, 
                                  export_draco_texcoord_quantization=12, 
                                  export_draco_color_quantization=10, 
                                  export_draco_generic_quantization=12, 
                                  export_tangents=False, 
                                  export_materials='EXPORT', # might change
                                  export_original_specular=False, # might change
                                  export_colors=True, 
                                  #export_attributes=False, 
                                  use_mesh_edges=False, 
                                  use_mesh_vertices=False, 
                                  export_cameras=False, 
                                  use_selection=False, 
                                  use_visible=False, 
                                  use_renderable=False, 
                                  #use_active_collection_with_nested=False, 
                                  use_active_collection=False, 
                                  use_active_scene=True, # might change
                                  export_extras=False, 
                                  export_yup=True, 
                                  export_apply=False, 
                                  export_animations=True, 
                                  export_frame_range=True, 
                                  export_frame_step=1, 
                                  export_force_sampling=True, 
                                  export_nla_strips=True, 
                                  export_nla_strips_merged_animation_name='Animation', 
                                  export_def_bones=False, 
                                  export_optimize_animation_size=False, 
                                  export_anim_single_armature=True, 
                                  #export_reset_pose_bones=True, 
                                  export_current_frame=False, 
                                  export_skins=True, 
                                  export_all_influences=False, 
                                  export_morph=True, 
                                  export_morph_normal=True, 
                                  export_morph_tangent=False, 
                                  export_lights=False, 
                                  will_save_settings=False, 
                                  filter_glob='*.glb;*.gltf')



        # send to API
        """
        filename = filePath + '.gltf'

        fp = open(filename, 'r')
        gltf = fp.read()

        gltf_json = json.loads(gltf)
        print(gltf_json, type(gltf_json))



        api_url = 'http://localhost:8080/' + name + '.gltf'
        test_response = requests.put(api_url, json = gltf_json)

        if test_response.ok:
            print("Upload completed successfully!")
            print(test_response.text)
        else:
            print("Something went wrong!")
            print(test_response.text)

        """

        return {'FINISHED'}