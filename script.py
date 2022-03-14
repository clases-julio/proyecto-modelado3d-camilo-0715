import bpy

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
''' M  A  I  N '''
'''************'''
if __name__ == "__main__":
    # Creación de un cubo y transformaciones de este:
    #Objeto.crearCubo('MiCubo')
    #Seleccionado.mover((0, 1, 2))
    #Seleccionado.escalar((1, 1, 2))
    #Seleccionado.escalar((0.5, 1, 1))
    #Seleccionado.rotarX(3.1415 / 8)
    #Seleccionado.rotarX(3.1415 / 7)
    #Seleccionado.rotarZ(3.1415 / 3)

    # Creación de un cono y transformaciones de este:
    #Objeto.crearCono('MiCono')
    #Activo.posicionar((-2, -2, 0))
    #Especifico.escalar('MiCono', (1.5, 2.5, 2))

    # Creación de una esfera y transformaciones de esta:
    #Objeto.crearEsfera('MiEsfera')
    #Especifico.posicionar('MiEsfera', (2, 0, 0))
    #Activo.rotar((0, 0, 3.1415 / 3))
    #Activo.escalar((1, 3, 1))
    
    borrarObjetos()
    Objeto.crearCubo('Cuepro')
    Seleccionado.mover((0, 0, 0.9))
    Seleccionado.escalar((1.5, 1.5, 1.6))
    
    Objeto.crearCylinder('Rueda_izq_interior')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, 0.45, 0.7))
    Seleccionado.escalar((0.5, 0.07, 0.5)) 
    
    Objeto.crearCylinder('Rueda_izq_medio')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, 0.55, 0.7))
    Seleccionado.escalar((0.4, 0.08, 0.4)) 
    
    Objeto.crearCylinder('Rueda_izq_exterior')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, 0.65, 0.7))
    Seleccionado.escalar((0.5, 0.07, 0.5)) 
    
    Objeto.crearCylinder('Rueda_der_interior')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, -0.45, 0.7))
    Seleccionado.escalar((0.5, 0.07, 0.5)) 
    
    Objeto.crearCylinder('Rueda_der_medio')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, -0.55, 0.7))
    Seleccionado.escalar((0.4, 0.08, 0.4)) 
    
    Objeto.crearCylinder('Rueda_der_exterior')   
    Seleccionado.rotarX(PI / 2)
    Seleccionado.mover((0, -0.65, 0.7))
    Seleccionado.escalar((0.5, 0.07, 0.5)) 
    
    
    Objeto.crearCubo('Cintura')
    Seleccionado.mover((0, 0, 1.4))
    Seleccionado.escalar((1, 1, 0.5))
    
    Objeto.crearCubo('Torax')
    Seleccionado.mover((0, 0, 1.7))
    Seleccionado.escalar((1.2, 1.9, 1))
    
    
    Objeto.crearEsfera('EsferaCuello')
    Seleccionado.rotarY(PI / 2)
    Seleccionado.mover((0.2, 0, 2))
    Seleccionado.escalar((0.6, 0.6, 0.6))
    
    Objeto.crearCylinder('CilindroCuello')
    Seleccionado.rotarY(PI / 2)
    Seleccionado.mover((0.3, 0, 2))
    Seleccionado.escalar((0.08, 0.3, 0.3))
    
    seleccionarObjeto('EsferaCuello')
    seleccionarObjeto('CilindroCuello')
    unirObjetos('cuello')
    
    Objeto.crearCubo('Cara')
    Seleccionado.mover((0.54, 0, 2))
    Seleccionado.escalar((0.3, 1.5, 1.5))
    

