import bpy
import requests
import tempfile
import os
import json

from bpy.types import Operator
from . lib import PageData, Cache


class CUSTOM_OT_Post_Operator(Operator):
    bl_idname = "object.post_to_server"
    bl_label = "Upload model"
    bl_description = "Post the model to the server"



    # defines if the operator should be enabled
    @classmethod
    def poll(cls, context):
        ais = context.scene.my_props.ais
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT" and ais > 1:
                return True

        return False

    def execute(self,context):

        jwt_resp = self.login(context)
        jwt_json = json.loads(jwt_resp.text)

        # invalid login
        if "message" in jwt_json:
            self.report({'ERROR'}, jwt_json['message'])
            return {'FINISHED'}


        jwt = jwt_json["token"]


        addResp = self.addModel(context, jwt)
        addResp_json = json.loads(addResp.text)

        # get response parameters and pass them
        mid = addResp_json["DATA"]["insertId"]
        uid = addResp_json["DATA"]["userId"]

        self.uploadModel(context,mid,uid, jwt)

        self.report({'INFO'},"Uploaded successfully")

        #TODO: reset input fields

        return {'FINISHED'}
    

    
    def login(self,context):

        data = {
            "uname": context.scene.my_props.uname,
            "pwd": context.scene.my_props.pwd
        }

        api_url = 'http://localhost:3001/login'

        response = None

        try:
            response = requests.post(url=api_url, data = data)

            if response.ok:
                print("Got JWT")
                
            else:
                print("Something went wrong!")
                


        except requests.exceptions.RequestException as e:
            self.report({'ERROR'}, "API error:" + e)
        

        return response




    def addModel(self, context, jwt):

        data = {
            "modName" : context.scene.my_props.mod_name,
            "modDesc" : context.scene.my_props.mod_desc,
            "artId" : context.scene.my_props.ais,
            "uname": context.scene.my_props.uname
        }

        headers = {
            "Authorization": "Bearer " + jwt
        }

        api_url = 'http://localhost:3001/model/add'

        response = None

        try:
            response = requests.post(url=api_url, data = data, headers=headers)

            if response.ok:
                print("Added into database!")
                
            else:
                print("Something went wrong!")
                print(response.text)
                


        except requests.exceptions.RequestException as e:
            self.report({'ERROR'}, "API error:" + e)
        

        return response





    def uploadModel(self, context, mid, uid, jwt):
        # make a temporary directory
        tempdir = tempfile.mkdtemp()
        file_ext = ".glb"


        file_name = "upload"

        filepath = os.path.join(tempdir, file_name)
        filepath += file_ext

        bpy.ops.export_scene.gltf(filepath=filepath, # might change
                                  check_existing=True, 
                                  #convert_lighting_mode='SPEC', 
                                  export_format='GLB', # might change
                                  ui_tab='GENERAL', 
                                  export_copyright=filepath, 
                                  export_image_format='AUTO', # might change
                                  export_texture_dir=filepath, # might change
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

        """
        bpy.ops.export_scene.fbx(filepath=filepath,
                                 check_existing=True,
                                 filter_glob='*.fbx', 
                                 use_selection=False, 
                                 use_visible=False, 
                                 use_active_collection=False, 
                                 global_scale=1.0, 
                                 apply_unit_scale=True, 
                                 apply_scale_options='FBX_SCALE_NONE', 
                                 use_space_transform=True, 
                                 bake_space_transform=False, 
                                 object_types={'ARMATURE','EMPTY', 'MESH', 'OTHER'}, 
                                 use_mesh_modifiers=True, 
                                 use_mesh_modifiers_render=True, 
                                 mesh_smooth_type='OFF', 
                                 #colors_type='SRGB', 
                                 #prioritize_active_color=False, 
                                 use_subsurf=False, 
                                 use_mesh_edges=False, 
                                 use_tspace=False, 
                                 use_triangles=False, 
                                 use_custom_props=False, 
                                 add_leaf_bones=True, 
                                 primary_bone_axis='Y', 
                                 secondary_bone_axis='X', 
                                 use_armature_deform_only=False, 
                                 armature_nodetype='NULL', 
                                 bake_anim=True, 
                                 bake_anim_use_all_bones=True, 
                                 bake_anim_use_nla_strips=True, 
                                 bake_anim_use_all_actions=True, 
                                 bake_anim_force_startend_keying=True, 
                                 bake_anim_step=1.0, 
                                 bake_anim_simplify_factor=1.0, 
                                 path_mode='AUTO', 
                                 embed_textures=False, 
                                 batch_mode='OFF', 
                                 use_batch_own_dir=True, 
                                 use_metadata=True, 
                                 axis_forward='-X', # default -Z
                                 axis_up='Z') # default Y
        """

        # add file extention for opening the file 
        # filepath = filepath + file_ext
        # read the binary file
        fp = open(filepath, 'rb')
        file = {'file' : (file_name + file_ext, fp, "multipart/form-data")}

        data = {
            "user" : uid,
            "model" : mid,
            "article" : context.scene.my_props.ais,
        }

        headers = {
            "Authorization": "Bearer " + jwt
        }


        api_url = 'http://localhost:3001/model/upload'

        response = None 

        try:
            response = requests.post(url=api_url, files=file, data = data, headers=headers)

            if response.ok:
                print("Upload completed successfully!")
                
            else:
                print("Something went wrong!")
                


        except requests.exceptions.RequestException as e:
            self.report({'ERROR'}, "API error:" + e)
            


        # clean up
        fp.close()

        os.remove(filepath)
        os.rmdir(tempdir)

        return response



def setFilter(self,context):
    # remove cached data
    Cache.articles = None



def parseArticleData(data):



    art_list = []

    for article in data['DATA']:
        id = str(article[PageData.COLUMN_01])
        name = article[PageData.COLUMN_02]
        # TODO: add description
        desc = "n/a"

        row = (id, name, desc)

        art_list.append(row)

    return art_list


def getArticles(self,context):

    articles = []

    # check cached data
    if Cache.articles != None:
        return Cache.articles



    fltr = self.fltr
    print(fltr)

    api_url = 'http://localhost:3001/article/list'
    data = {
        "filter": fltr 
    }

    try:
        response = requests.get(url=api_url, params = data)

        if response.ok:
            print("Fetched articles successfully!")
            response_json = json.loads(response.text)

            # fill the article select dropdown
            articles = parseArticleData(response_json)

            # cache articles
            Cache.articles = articles

            return articles



        else:
            print("Cannot fetch articles!")
            print(response.text)

            return articles

    except requests.exceptions.RequestException as e:
        print({'ERROR'}, e)

        return articles
    




class CUSTOM_OT_Article_Operator(Operator):
    bl_idname = "object.select_article"
    bl_label = "Select article"
    bl_description = "select the article you are uploading the model for"


    fltr : bpy.props.StringProperty(name="Filter:", update=setFilter)
    slct : bpy.props.EnumProperty(items=getArticles, name="Select article")

    # defines if the operator should be enabled
    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True

        return False

    def execute(self,context):


        context.scene.my_props.ais = int(self.slct)
        context.scene.my_props.art_name = self.getArticleName()


        return {'FINISHED'}
    

    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)
    

    def getArticleName(self):

        out = "No article selected"

        for art in Cache.articles:
            if int(art[0]) == int(self.slct):
                out = art[1]
                break

        return out
