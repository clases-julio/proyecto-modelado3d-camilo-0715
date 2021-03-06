import bpy
from bpy import context, data, ops

PI = 3.1415

'''*********************************************************************'''
'''Funciones comunes útiles para selección/activación/borrado de objetos'''
'''*********************************************************************'''
def seleccionarObjeto(nombreObjeto): # Seleccionar un objeto por su nombre
    bpy.ops.object.select_all(action='DESELECT') # deseleccionamos todos...
    bpy.data.objects[nombreObjeto].select = True # ...excepto el buscado

def activarObjeto(nombreObjeto): # Activar un objeto por su nombre
    bpy.context.scene.objects.active = bpy.data.objects[nombreObjeto]

def borrarObjeto(nombreObjeto): # Borrar un objeto por su nombre
    seleccionarObjeto(nombreObjeto)
    bpy.ops.object.delete(use_global=False)

def borrarObjetos(): # Borrar todos los objetos
    if(len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
def unirObjetos(objName):
    bpy.ops.object.join()
    Activo.renombrar(objName)
    
def deseleccionarObjetos(): 
    bpy.ops.object.select_all(action='DESELECT')

def seleccionarObjeto(nombreObjeto): # Seleccionar un objeto por su nombre
    bpy.data.objects[nombreObjeto].select_set(True)
    
def cambiarcolor(r, g, b,ColorName):
    
    r = r/ 255
    g = g / 255
    b = b/ 255
    
    activeObject = bpy.context.active_object
    material = bpy.data.materials.new(name=ColorName)
    activeObject.data.materials.append(material)
    bpy.context.object.active_material.diffuse_color = (r , g, b, 1)
    
def setImageTexture(ImagePath,TextureName):
    #activeObject = bpy.context.active_object
    
    image = bpy.ops.image.open(filepath="//cara.jpg", directory="/home/alumnos/camilo/Escritorio/universidad/curso3/modelado/blender/proyecto-modelado3d-camilo-0715/", files=[{"name":"cara.jpg", "name":"cara.jpg"}], show_multiview=False)
    
    mat = bpy.data.materials.new(name=TextureName)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(ImagePath)
    mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

    ob = context.view_layer.objects.active
    ob.data.materials.append(mat)


'''****************************************************************'''
'''Clase para realizar transformaciones sobre objetos seleccionados'''
'''****************************************************************'''
class Seleccionado:
    def mover(v):
        bpy.ops.transform.translate(
            value=v, constraint_axis=(True, True, True))

    def escalar(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))

    def rotarX(v):
        bpy.ops.transform.rotate(value=v, orient_axis='X')

    def rotarY(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Y')

    def rotarZ(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Z')

'''**********************************************************'''
'''Clase para realizar transformaciones sobre objetos activos'''
'''**********************************************************'''
class Activo:
    def posicionar(v):
        bpy.context.object.location = v

    def escalar(v):
        bpy.context.object.scale = v

    def rotar(v):
        bpy.context.object.rotation_euler = v

    def renombrar(nombreObjeto):
        bpy.context.object.name = nombreObjeto

'''**************************************************************'''
'''Clase para realizar transformaciones sobre objetos específicos'''
'''**************************************************************'''
class Especifico:
    def escalar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].scale = v

    def posicionar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].location = v

    def rotar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].rotation_euler = v

'''************************'''
'''Clase para crear objetos'''
'''************************'''
class Objeto:
    def crearCubo(objName):
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)

    def crearEsfera(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)

    def crearCono(objName):
        bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)
        
    def crearCylinder(objName):
        bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
        Activo.renombrar(objName)
        
        
'''************'''
''' FUNCIONES PARA CREAR EL ROBOT '''
'''************'''
        
def CrearCuerpo():
    Objeto.crearCubo('Cintura')
    Seleccionado.mover((0, 0, 1.4))
    Seleccionado.escalar((1, 1, 0.5))
    cambiarcolor(50,50,50, 'ColorCintura')
    
    Objeto.crearCubo('Torax')
    Seleccionado.mover((0, 0, 1.7))
    Seleccionado.escalar((1.2, 1.6, 1))
    cambiarcolor(255,255,255, 'ColorTorax')
    
    seleccionarObjeto('Cintura')
    seleccionarObjeto('Torax')
    
    unirObjetos('CuerpoMedio')
    
    Objeto.crearCubo('Cuerpo')
    Seleccionado.mover((0, 0, 0.9))
    Seleccionado.escalar((1.5, 1.5, 1.6))
    Seleccionado.rotarX(PI / 2)
    setImageTexture("/home/alumnos/camilo/Escritorio/universidad/curso3/modelado/blender/proyecto-modelado3d-camilo-0715/urjc_pequeno.png","textura cuerpo")
    

    


def CrearRuedas():

    Objeto.crearCylinder('RuedaIzqInterior')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, 0.45, 0.7))
    Seleccionado.escalar((0.5, 0.07, 0.5)) 
    
    Objeto.crearCylinder('RuedaIzqMedio')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, 0.55, 0.7))
    Seleccionado.escalar((0.4, 0.08, 0.4)) 
    
    Objeto.crearCylinder('RuedaIzqExterior')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, 0.65, 0.7))
    Seleccionado.escalar((0.5, 0.07, 0.5)) 
    
    seleccionarObjeto('RuedaIzqInterior')
    seleccionarObjeto('RuedaIzqMedio')
    seleccionarObjeto('RuedaIzqExterior')
    
    unirObjetos('RuedaIzq')
    cambiarcolor(50,50,50,'ColorRuedaIzq')
    
    Objeto.crearCylinder('RuedaDerInterior')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, -0.45, 0.7))
    Seleccionado.escalar((0.5, 0.07, 0.5)) 
    
    Objeto.crearCylinder('RuedaDerMedio')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, -0.55, 0.7))
    Seleccionado.escalar((0.4, 0.08, 0.4)) 
    
    Objeto.crearCylinder('RuedaDerExterior')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, -0.65, 0.7))
    Seleccionado.escalar((0.5, 0.07, 0.5)) 
    
    seleccionarObjeto('RuedaDerInterior')
    seleccionarObjeto('RuedaDerMedio')
    seleccionarObjeto('RuedaDerExterior')
    
    unirObjetos('RuedaDer')
    cambiarcolor(50,50,50,'ColorRuedaDer')


def CrearCabeza():
    Objeto.crearEsfera('EsferaCuello')
  
    Seleccionado.mover((0.2, 0, 2))
    Seleccionado.escalar((0.6, 0.6, 0.6))
    
    Objeto.crearCylinder('CilindroCuello')
    Seleccionado.rotarY(PI / 2)
    Seleccionado.mover((0.3, 0, 2))
    Seleccionado.escalar((0.08, 0.3, 0.3))
    
    seleccionarObjeto('EsferaCuello')
    seleccionarObjeto('CilindroCuello')
    unirObjetos('Cuello')
    cambiarcolor(50,50,50, 'ColorCuello')
    
    Objeto.crearCubo('Cara')
    Seleccionado.mover((0.54, 0, 2))
    Seleccionado.rotarX(PI / 2)
    Seleccionado.escalar((0.3, 1.5, 1.5))
    setImageTexture("/home/alumnos/camilo/Escritorio/universidad/curso3/modelado/blender/proyecto-modelado3d-camilo-0715/cara.jpg","textura cara")
    

def CrearManos():
    Objeto.crearEsfera('HombroIzq')
    Seleccionado.mover((0, 0.4, 1.7))
    Seleccionado.escalar((0.35, 0.35, 0.35))
    cambiarcolor(50,50,50, 'ColorHombro')
    
    Objeto.crearCylinder('BrazoIzq')
    Seleccionado.mover((0.25, 0.5, 1.5))
    Seleccionado.escalar((0.06, 0.06, 0.35))
    Seleccionado.rotarX(PI / 2)
    Seleccionado.rotarZ(PI / 2 -0.1)
    Seleccionado.rotarY(-0.8)
    cambiarcolor(255,255,255, 'ColorBrazo')
    
    Objeto.crearEsfera('Codo')
    Seleccionado.mover((0.5, 0.55, 1.25))
    Seleccionado.escalar((0.2, 0.2, 0.2))
    cambiarcolor(50,50,50, 'ColorCuello')
    
    Objeto.crearCylinder('BrazoIzq')
    Seleccionado.mover((0.65, 0.4, 1.28))
    Seleccionado.escalar((0.05, 0.05, 0.25))
    Seleccionado.rotarX(PI / 2 + 0.5)
    Seleccionado.rotarZ(PI / 2 + 1)
    Seleccionado.rotarY(1)
    cambiarcolor(255,255,255, 'ColorBrazo')
    
    Objeto.crearEsfera('MunezaIzq')
    Seleccionado.mover((0.83, 0.195, 1.31))
    Seleccionado.escalar((0.12, 0.12, 0.12))
    cambiarcolor(50,50,50, 'ColorMuneca')
    
    Objeto.crearCubo('DedoIzq1')
    Seleccionado.mover((0.93, 0.19, 1.35))
    Seleccionado.escalar((0.25, 0.2, 0.05))
    
    Objeto.crearCubo('DedoIzq2')
    Seleccionado.mover((0.77, 0.195, 1.35))
    Seleccionado.escalar((0.25, 0.2, 0.05))
    
    Objeto.crearCubo('DedoIzq3')
    Seleccionado.mover((0.85, 0.1, 1.35))
    Seleccionado.escalar((0.25, 0.2, 0.05))
    Seleccionado.rotarZ(PI/2)
    
    
    Objeto.crearEsfera('HombroDer')
    Seleccionado.mover((0, -0.4, 1.7))
    Seleccionado.escalar((0.35, 0.35, 0.35))
    cambiarcolor(50,50,50, 'ColorHombro')
    
    Objeto.crearCylinder('BrazoDer')
    Seleccionado.mover((0.25, -0.5, 1.5))
    Seleccionado.escalar((0.06, 0.06, 0.35))
    Seleccionado.rotarX(PI / 2)
    Seleccionado.rotarZ(-PI / 2 +0.1)
    Seleccionado.rotarY(-0.8)
    cambiarcolor(255,255,255, 'ColorBrazo')
    
    Objeto.crearEsfera('CodoDer')
    Seleccionado.mover((0.5, -0.55, 1.25))
    Seleccionado.escalar((0.2, 0.2, 0.2))
    cambiarcolor(50,50,50, 'ColorCodo')
    
    Objeto.crearCylinder('AnteBrazoDer')
    Seleccionado.mover((0.65, -0.4, 1.28))
    Seleccionado.escalar((0.05, 0.05, 0.25))
    Seleccionado.rotarX(-PI / 2 - 0.5)
    Seleccionado.rotarZ(-PI / 2 - 1)
    Seleccionado.rotarY(1)
    cambiarcolor(255,255,255, 'ColorBrazo')
    
    Objeto.crearEsfera('MunezaIzq')
    Seleccionado.mover((0.83, -0.195, 1.31))
    Seleccionado.escalar((0.12, 0.12, 0.12))
    cambiarcolor(50,50,50, 'ColorMuneca')
    
    Objeto.crearEsfera('MunezaIzq')
    Seleccionado.mover((0.83, 0.195, 1.31))
    Seleccionado.escalar((0.12, 0.12, 0.12))
    cambiarcolor(50,50,50, 'ColorMuneca')
    
    Objeto.crearCubo('DedoIzq1')
    Seleccionado.mover((0.93, -0.19, 1.35))
    Seleccionado.escalar((0.25, 0.2, 0.05))
    
    Objeto.crearCubo('DedoIzq2')
    Seleccionado.mover((0.77, -0.195, 1.35))
    Seleccionado.escalar((0.25, 0.2, 0.05))
    
    Objeto.crearCubo('DedoIzq3')
    Seleccionado.mover((0.85, -0.1, 1.35))
    Seleccionado.escalar((0.25, 0.2, 0.05))
    Seleccionado.rotarZ(PI/2)
    
    
    Objeto.crearCubo('Bandeja')
    Seleccionado.mover((0.9, 0, 1.4))
    Seleccionado.escalar((0.8, 1.5, 0.1))
    cambiarcolor(120,120,120,'ColorBandeja')
    

    
def jaggerbottle():
    
    Objeto.crearCubo('BottleBody')
    Seleccionado.mover((1, 0.2, 1.55))
    Seleccionado.escalar((0.15, 0.55, 0.4))
    Seleccionado.rotarX(PI/2)
    
    setImageTexture("/home/alumnos/camilo/Escritorio/universidad/curso3/modelado/blender/proyecto-modelado3d-camilo-0715/jaggerSkin.png","texturajagger")
    
    Objeto.crearCubo('Pitote')
    Seleccionado.mover((1, 0.2, 1.6))
    Seleccionado.escalar((0.1, 0.1, 0.55))
    cambiarcolor(20,20,20, 'ColorPitote')
   
'''************'''
''' M  A  I  N '''
'''************'''
if __name__ == "__main__":
    
    
    borrarObjetos()
    
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 8, 2),rotation=(PI/2 - 0.08 , 0, PI))

    bpy.ops.object.light_add(type='SUN', radius=1, location=(0, 0, 10))
    
    #creamos las ruedas
    CrearRuedas()
    
    #creamos el cuerpo
    CrearCuerpo()
    
    #creamos la cabeza
    CrearCabeza()
    
    #creamos las manos
    CrearManos()
    
    jaggerbottle()

    
    


