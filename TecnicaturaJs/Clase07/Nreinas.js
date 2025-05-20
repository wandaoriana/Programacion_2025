// Problema de las N Reinas en JavaScript
// Resuelve el problema para N=8 (puedes cambiar el valor de N)
// Muestra el tablero en consola cada vez que se coloca una reina
// Al final, imprime el tablero final y el arreglo de índices de las reinas

const N = 8; // Puedes cambiar este valor a cualquier N >= 8

// Función para imprimir el tablero en consola
// Imprime 'Q' donde hay una reina y '.' donde está vacío
function imprimirTablero(tablero) {
  for (let fila = 0; fila < N; fila++) {
    let linea = '';
    for (let columna = 0; columna < N; columna++) {
      linea += tablero[fila][columna] ? 'Q ' : '. ';
    }
    console.log(linea);
  }
  console.log('\n');
}

// Función para verificar si es seguro colocar una reina en tablero[fila][columna]
// Revisa columna, diagonal superior izquierda y diagonal superior derecha
function esSeguro(tablero, fila, columna) {
  // Revisar esta columna en filas anteriores
  for (let i = 0; i < fila; i++) {
    if (tablero[i][columna]) return false;
  }
  // Revisar diagonal superior izquierda
  for (let i = fila - 1, j = columna - 1; i >= 0 && j >= 0; i--, j--) {
    if (tablero[i][j]) return false;
  }
  // Revisar diagonal superior derecha
  for (let i = fila - 1, j = columna + 1; i >= 0 && j < N; i--, j++) {
    if (tablero[i][j]) return false;
  }
  return true;
}

// Arreglo para guardar la posición de cada reina
// solucion[fila] = columna donde está la reina en esa fila
let solucion = Array(N).fill(-1);

// Función principal de backtracking para resolver el problema
// Intenta colocar una reina en cada fila
function resolverNReinas(tablero, fila) {
  // Caso base: si se colocaron todas las reinas, retorna true
  if (fila === N) {
    // Solución encontrada
    return true;
  }
  // Intentar colocar una reina en cada columna de la fila actual
  for (let columna = 0; columna < N; columna++) {
    if (esSeguro(tablero, fila, columna)) {
      // Colocar la reina
      tablero[fila][columna] = 1;
      solucion[fila] = columna;
      // Mostrar el tablero actual
      console.log(`Colocando reina en fila ${fila}, columna ${columna}`);
      imprimirTablero(tablero);
      // Llamada recursiva para la siguiente fila
      if (resolverNReinas(tablero, fila + 1)) {
        return true;
      }
      // Si no se puede, quitar la reina (backtrack)
      tablero[fila][columna] = 0;
      solucion[fila] = -1;
    }
  }
  // Si no se puede colocar ninguna reina en esta fila, retorna false
  return false;
}

// Inicializar el tablero vacío (matriz de NxN con ceros)
let tablero = Array.from({ length: N }, () => Array(N).fill(0));

// Ejecutar el algoritmo y mostrar resultados
if (resolverNReinas(tablero, 0)) {
  console.log('Tablero final:');
  imprimirTablero(tablero);
  console.log('Índices de las reinas por fila (columna):', solucion);
} else {
  console.log('No hay solución para N =', N);
}
