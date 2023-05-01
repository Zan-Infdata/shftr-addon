import bpy

class My_Properties(bpy.types.PropertyGroup):
    uname : bpy.props.StringProperty(
        name='Username',
        description='Enter your Shapeshifter account username',
    )

    pwd : bpy.props.StringProperty(
        name='Password',
        description='Enter your Shapeshifter account password',
        subtype = 'PASSWORD',
    )

    ais : bpy.props.IntProperty(
        name='ArtIsSet',
        description='Check if article is set',
        default=-1,

    )

    art_name : bpy.props.StringProperty(
        name='ArtName',
        description='Selected article name',
        default='No article selected'

    )

    mod_name : bpy.props.StringProperty(
        name='Model name',
        description='Your model name',
        default='Model name'
    )

    mod_desc : bpy.props.StringProperty(
        name='Model description',
        description='Your model description',
        default='Model description'
    )

def initUsernameProperty():
    out = bpy.props.StringProperty(
        name='Username',
        description='Enter your Shapeshifter account username',
    )
    return out

def initPasswordProperty():
    out = bpy.props.StringProperty(
        name='Password',
        description='Enter your Shapeshifter account password',
        subtype = 'PASSWORD',
    )
    return out

def initArtIsSetProperty():
    out = bpy.props.IntProperty(
        name='ArtIsSet',
        description='Check if article is set',
        default=-1,

    )
    return out





