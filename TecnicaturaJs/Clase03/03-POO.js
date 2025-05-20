class Empleado {     // polimorfismo 
    constructor(nombre, sueldo){
        this._nombre = nombre;
        this._sueldo = sueldo;
    }

    obtenerDetalles(){
        return `Empleado: nombre: ${this._nombre},
                sueldo: ${this._sueldo}`;
    }    
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre, sueldo);
        this._departamento = departamento;
    }

    //Agregamos la sobreescritura
    obtenerDetalles(){
        return `Gerente: ${super.obtenerDetalles()} depto: ${this._departamento}`;
    }
}

function imprimir( tipo ) {
    console.log( tipo.obtenerDetalles());
    if( tipo instanceof  Gerente) {     //tipo gerente
        console.log('Es un objeto de tipo Gerente');
        console.log(tipo._departamento);
    }

    
    else if( tipo instanceof Empleado){    //tipo empleado
        console.log('Es de tipo Empleado'); 
    }

    else if( tipo instanceof Object){ //clase padre de todas las clases 
    }
}


let gerente1 = new Gerente("Carlos", 5000, "Sistemas");
console.log(gerente1); //Objeto de la clase hija

let empleado1 = new Empleado("Juan", 3000);
console.log(empleado1) //Objeto de la clase padre

imprimir( gerente1 );

imprimir ( empleado1 ); 
