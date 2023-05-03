# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from . ca_property import My_Properties
from . ca_operator import CUSTOM_OT_Post_Operator, CUSTOM_OT_Article_Operator
from . ca_panel import CUSOTM_PT_Panel


_classes = [CUSTOM_OT_Post_Operator, CUSTOM_OT_Article_Operator, CUSOTM_PT_Panel, My_Properties  ]

bl_info = {
    "name" : "Shapeshifter_addon",
    "author" : "Zan",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "VIEW_3D",
    "warning" : "",
    "category" : "object"
}




def register():

    for cls in _classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.my_props = bpy.props.PointerProperty(type=My_Properties)

def unregister():

    del bpy.types.Scene.my_props


    for cls in _classes:
        bpy.utils.unregister_class(cls)
