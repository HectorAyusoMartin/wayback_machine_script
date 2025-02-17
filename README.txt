Este script realizado en Python, a través de la webapp Wayback machine, intenta automatizar el proceso de busqueda de una aplicación web en un rango
de tiempo elegido, con la intención de hacer una enumeración OSINT de dominio y subdominios, dentro del marco de una auditoria de seguridad, 
para buscar información relevante que actualmente ha podido cambiar o haya sido eliminada de una aplicación web objetivo.

La idea es automatizar el proceso debido a la tediosidad de hacer esto a mano, y la gran demora de respuesta que produce Wayback machine en su uso
a través de su aplicación Web.

Se ha incorpordado una nuieva funcion para a traves de una expresión regular, filtrar y descargar los datos por extension de archivo. ( def search_snapshots_by_extensions: )



Existe la biblioteca llamada waybackpy, mas concretamente el módulo WaybackMachineCDXServerAPI, para el manejo interno de la webapp con el script.
