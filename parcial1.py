productos= {
0:{'Dulce':[0.05,"bolsa",30]},
1:{'Pan':[0.15,"unidad",50]},
2:{'leche':[2.50,"galon",10]},
3:{'queso':[3.0,"libra",10]},
4:{'frijol':[0.78,"libra",200]},
5:{'arroz':[0.40,"libra",100]},
6:{'serial':[3.40,"caja",100]},
7:{'jabon':[0.80,"unidad",30]},
8:{'embutidos':[1.20,"libra",55]},


}

def buscar():
    valor=raw_input("buscar:")
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if k== valor:
                print k
                print"el producto si existe =", productos.has_key(k1)
                print "precio:",v[0]
                print "pos:",v[1]
                print "existencia:",v[2]

def ven():
    
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if k:
                print k
                print "precio:",v[0]
                print "existencia:",v[2]
                print ""                                
def ven1():
    valor=raw_input("producto a vender: ")
    cantidad=int(raw_input("cantidad a vender:"))
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if k== valor:
                print k
                print "precio:",v[0]
                print "existencia:",v[2]-cantidad               
def modificar():
    valor=raw_input("producto a vender: ")
    pos = int(raw_input("editar posicion: "))
    produ = raw_input("producto: ")
    a = int(raw_input("precio: "))
    b = raw_input("pos: ")
    c = int(raw_input("cantidad: "))
    
    for k1 in productos.keys():
        for k, a,b,c in productos[k1].iteritems():
            if k== valor:
                productos[pos]= {produ:[a[0],b[1],c[2]]}
                
    
                                              
                                                                        
while True:
    print "1 - busqueda del producto"
    print "2 - modificar producto"
    print "3 - eliminar la entrada del producto"
    print "4 - ventas de producto"
    print "5 - Salir"
    
    opcion = int(raw_input("Seleccione opcion: "))
    
    if opcion == 1:
        buscar()
               
    elif opcion == 2:
     pos = int(raw_input("editar posicion: "))
     produ = raw_input("producto: ")
     a = int(raw_input("precio: "))
     b = raw_input("pos: ")
     c = int(raw_input("cantidad: "))
     
     productos[pos]=produ
     productos[pos]={produ:[a]}
     productos[pos]={produ:[a,b]}
     productos[pos]={produ:[a,b,c]}
     
     print productos 
    
    elif opcion == 3:
        eliminar = int(raw_input("elimina la posicion: "))
        del productos[eliminar]
        print productos
    elif opcion == 4:
        print ""
        print "productos disponibles"
        print ""
        ven()
        print ""
        ven1()
    elif opcion == 5:            
       break      
    