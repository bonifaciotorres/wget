import os
import os.path
from os import popen
print "----------------ADVERTENCIA---------------------"
print "-------LEA DETENIDAMENTE CADA OPCION------------"
print ""
print "opcion 1: crea los directorio con el ejemplo de la url que se muestra en ella"
print "opcion 1: al momento de crear el url HTML se debe crear dos mas de la misma manera"
print "opcion 1: en la ruta aparece el nombre del usuario bonifacio sola mente se intercambia por su usuario"
print "opcion 1: ejemplo:/home/bonifacio/Escritorio/HTML/html y otra vez la misma direccion pero el html en minusculas lo sustituimos por IMG"
print "opcion 2: se realizara exitosamente si se completo con exito el paso 1"
print "opcion 3: colocar archivo html de la imagen luego busquelo en el directorio HTML/IMG la imagen que descargo"
print "opcion 4: se ejecuta exitosamente si se creo la opcion 1 exitosamente"
print "opcion 4: antes de ejecutar la opcion debera tener abierto su navegador firefox por causas de un bug que si no esta abierto solo abre una pagina "
print"--------------------------------------------------"
print ""

while True:
    
    print "1 - Crear directorio de trabajo"
    print "2 - Descargar sitio HTML"
    print "3 - Descargar archivo con extension de imagenes"
    print "4 - Buscar archivo HTML"
    print "5 - Mostrar la capacidad de mega bite"
    print "6 - Salir"
    
    opcion = int(raw_input("Seleccione opcion: "))
    
    if opcion == 1:
        print "1 - Crear directorio con permisos incluidos"
        print "2 - existencia del directorio"
        
    
    
        opcion = int(raw_input("Seleccione opcion: "))
        if opcion==1:
	    print "utilise la ruta de ejemplo:/home/bonifacio/Escritorio/NOMBRE DEL DIRECTORIO"     #dado el caso de la direccion de mi pc 
            d=raw_input("escriba el nombre de directorio:")
            os.mkdir(d,0o777)
            print "Los permisos se crearon con exito"
            print ""
        elif opcion==2:
              print"quiere saber si su directorio ya existe"
	      e=raw_input("el nombre de la directorio :")
	      if os.path.exists(e):
	          print "existe"
	      else:
	          print"no existe"    
	      			
    elif opcion == 2:
        
        
       # url = 'http://docs.python.org.ar/tutorial/3/index.html'
        #location = '/home/bonifacio/Escritorio/html/'
        #args = ['wget','-r', '-l 1', '-p','-P' , location, url]
        #output = popen(' '.join(args))
	d='http://docs.python.org.ar/tutorial/3/index.html'
	dD='http://docs.python.org.ar/tutorial/3/index.html'
        l = '/home/bonifacio/Escritorio/HTML/IMG'
        lL = '/home/bonifacio/Escritorio/HTML/html'
        imagen = ['wget','-r', '-l1','-np','-nd','-A.jpg,.png,.gif','-N','-P', l, dD]
        imagen1 = ['wget','-r', '-l1','-np','-nd','-A.html','-N','-P' , lL, d]
        output = popen(' '.join(imagen))
	output = popen(' '.join(imagen1))		
    elif opcion == 3:
        d=raw_input("ingrese su url:")
        l = '/home/bonifacio/Escritorio/HTML/IMG'
        imagen = ['wget','-r', '-l1','-np','-nd','-A.jpg,.png,.gif','-N','-P' , l, d]
        output = popen(' '.join(imagen))
        
    elif opcion == 4:
        print "puede probar con esta imagen:https://pbs.twimg.com/profile_images/478947556760645632/IwdfeL3J_400x400.png"
        D= '/home/bonifacio/Escritorio/HTML/html/errors.html'
        DX= '/home/bonifacio/Escritorio/HTML/html/interpreter.html'
        os.system('firefox '+D)
        os.system('firefox '+DX)		
    elif opcion == 5:
        
        print "NO LO PUDE HACER"
       
    elif opcion == 6:
        break     
