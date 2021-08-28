# DS-HTTP
Reto numero 2 topicos especiales en telemática

### Integrantes:

- Isabel Piedrahita
- Santiago Santacruz
- Duvan andres ramirez


## 1. Especificación del Servicio

El presente es un servicio de acortar, verificar el status y generar codigo binario de codigo QR para links de internet. Esto se hizo con la intención de que el usuario pueda enviar los links al servidor para después generar unos más cortos, tener el conocimiento de la pagina por terminal para su uso y tener el codigo QR de dicha pagina.

Para efectos de facilidad de uso se desarrolló una shell interactiva llamada ShortyShell para el cliente, en la que se implementaron además de los comandos básicos de ShortyShell comandos de ayuda para el usuario. Estos comandos de ayuda listan la sintaxis correcta de cada una de estas operaciones y explican lo que cada una hace. Las instrucciones para llamar a estas ayudas son visibles cuando el cliente accede a ShortyShell.

Finalmente, algunas consideraciones adicionales sobre el servicio. El comportamiento del servidor se presta para manejar a multiples clientes de manera concurrente por medio de threads, cada cliente puede conectarse y desconectarse del servidor en el momento que lo considere. Por último, para garantizar la transparencia en operaciones. (falta implementacion de LOG).


## 2. Vocabulario del Mensaje

ShortyShell utiliza una misma estructura de mensaje para todas sus comunicaciones;
| Mensaje | Descripción   |
|------|------|
| SHORT <URL> | Recorta un URL  |
| STATUS <URL> | Estado de la pagina |
| REQUESTS | Lista todos los Requests hechos, teniendo en cuenta Request |
| QR | Retorna el codigo binario de la pagina para sacar su QR  de este |
| bye | termina la sesión |

## 3. Regla de Procedimientos

La estructura general del protocolo se explica en el siguiente diagrama.

![image](https://user-images.githubusercontent.com/46933082/131228396-8004a577-9428-4661-aa9b-dc2ebcc012b8.png)





Los mensajes que puede enviar el cliente están definidos de la siguiente forma. En la tabla verá significado semántico en la columna de procedimiento, mientras que en la columna de URL encontrará el URL correspondiente, en la que es muy fácil deducir a que se refiere el código y por ende no se pondrá entre paréntesis su significado. Todas estas peticiones de cliente son independientes entre si y el servidor no requiere mantener información de estado para manejar estas.

Los mensajes recibidos son todos muy similares en estructura, contienen un output que representa la información que se le debe mostrar al cliente. Este output es una string. Siempre que se envía un mensaje, se debe esperar un mensaje de respuesta.

Los errores en ShortyShell se manejan mediante la captura de excepciones, hay principalmente tres tipos de error, error de conección y error en tipo de dato. Los errores de coneccion se manejan levantando una excepción de tipo RuntimeError("socket connection broken"), no retornan nada al cliente. Los mensajes de falla en tipo de dato se manejan capturando la excepción y retornando al usuario un mensaje de error que quiere decir que alguno de los valores ingresados no se encuentra en la forma correcta.A continuación hay una tabla con cada error y los mensajes que imprime en la consola interactiva.
| Error | Mensaje   |
|------|------|
| Error de conexión | 400  |
| Error de comando| Lo sentimos, no estamos esperando <code>|

### 4. Regla de protocolo

Para la comunicacion entre los diferentes nodos y cliente, al manejarlo por un IPC de tipo independiente, el cual no se ve afectada la ejecuccion de los otros procesos mientras esta cooperando. El Inter-process comunication (IPC), es el mecanismo el cual nos permite cominicarnos y sincronizar las acciones entre los diferentes nodos. En nuestra arquitectura de comunicacion, estamos usando el protocolo HTTP, que se está soportado sobre los servicios de conexión TCP/IP. El protocolo funciona de la siguiente manera: un proceso servidor escucha en un puerto de comuniaciones TCP, y espera las solicitudes de conexión de los clientes Web. una vez se establece la conexión, el protocolo TCP se encarga de mantener la comunicación. El protocolo se basa en operaciones solicitud/respuesta. 

### 5. Etapas de transacción del protocolo

  1. Un usuario solicita un servicio (REQUESTS, SHORT, QR, STATUS). La solicitud del servicio genera una URL con la informacion de la petición.
  2. El Cliente identifica el protocolo de acceso, la dirección DNS, el puerto y el objeto requerido del servidor.
  3. Se abre una conexión TCP/IP con el servidor llamando al puerto TCP 3000 y se envia la petición con el comando GET o POST dependiendo del servicio.
  4.El servidor devuelve la respuesta al cliente. Que Consiste en un código de estado y el tipo de dato MIME de la información de retorno, seguido de la propia información.
  5. Se cierra la conexión TCP. 

 #### NOTA: Este proceso se repite en cada acceso al servidor.
