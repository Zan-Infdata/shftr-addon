import bpy

from bpy.types import Panel

class CUSOTM_PT_Panel(Panel):
    bl_space_type= "VIEW_3D"
    bl_region_type= "UI"
    bl_label = "Shapeshifter uploader"
    bl_category = "Shapeshifter"

    

    def draw(self,context):
        

        layout = self.layout

        my_props = context.scene.my_props
        
        row = layout.row()
        row.label(text="Login", icon = "EXPORT")

        box = layout.box()
        
        row = box.row()
        col = row.column()
        col.prop(my_props, 'uname')


        row = box.row()
        col = row.column()
        col.prop(my_props, 'pwd')

    

        row = layout.row()
        row.label(text="Select article")


        box = layout.box()
        row = box.row()
        self.art_name = row
        row.label(text=(my_props.art_name).upper())
        col = row.column()
        col.operator("object.select_article")


        row = layout.row()
        row.label(text="About model")


        box = layout.box()

        row = box.row()
        col = row.column()
        col.prop(my_props, 'mod_name')
        
        row = box.row()
        col = row.column()
        col.prop(my_props, 'mod_desc')        

        row = layout.row()
        col = row.column()
        col.operator("object.post_to_server")
        
        