import bpy

from bpy.types import Panel

class CUSOTM_PT_Panel(Panel):
    bl_space_type= "VIEW_3D"
    bl_region_type= "UI"
    bl_label = "Custom addon"
    bl_category = "Custom ADDON"


    def draw(self,context):
        
        layout = self.layout

        row = layout.row()
        col = row.column()

        col.operator("object.post_to_server", text="Post to server")