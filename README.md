# Tres reglas, un tablado, una rebelión

Guía visual e interactiva para una clase de **Introducción a la Literatura** sobre las unidades aristotélicas, el corral de comedias y la ruptura del teatro barroco español (Lope de Vega y el *Arte nuevo de hacer comedias*, 1609).

## Cómo abrirla

Abre `teatro-barroco-unidades.html` con doble clic. Es un archivo autónomo: todo el CSS, el JavaScript y los diagramas SVG están incluidos. Solo las tipografías (Fraunces y Manrope) se cargan desde Google Fonts; sin conexión, el navegador usa serif y sans de respaldo.

## Qué incluye

1. **Portada** con el decreto satírico de las tres unidades.
2. **La tríada**: acción, tiempo y lugar; el *plot twist* de que la doctrina es una codificación renacentista y neoclásica, no una cita literal de Aristóteles.
3. **Simulador de unidades**: tres perillas (lugares, tiempo, tramas) con certificado y veredicto en vivo.
4. **Plano interactivo del corral**: ocho zonas (tablado, patio, cazuela, aposentos, desván, foso, alojería, toldo) y su efecto en la dramaturgia.
5. **Lope y el *Arte nuevo***: seis movimientos con cita, traducción a lenguaje actual y efecto; polimetría; lo que Lope no rompió; línea de tiempo.
6. **Comparación Atenas / corral** en tabla.
7. **Cuatro obras** analizadas con las unidades marcadas.
8. **Chat ficticio del Siglo de Oro**, resumen y **quiz de 7 preguntas** con explicaciones.
9. **Glosario** de 17 términos y **plan de clase de 45 minutos** con actividad, discusión, objetivos y citas.
10. **Imprimir / guardar PDF** desde el bloque “Para el aula”.

## Si los clics no responden

Las capturas y las tarjetas de vista previa del chat son imágenes: no ejecutan nada. Además, el botón **Probar el simulador** no abre una ventana: baja hasta la sección del simulador. Si el visor bloquea el scroll suave, ahora hay un salto instantáneo de respaldo y un destello dorado en la sección.

Para usar la versión interactiva:

1. Abre `teatro-barroco-unidades.html` con doble clic en Finder, o arrástralo a Chrome, Safari o Firefox.
2. Si lo estás viendo dentro de una vista incrustada, pulsa **Abrir en pestaña** en el aviso superior.
3. Si aparece la tarjeta crema **«JavaScript no está corriendo en este visor»**, el visor tiene el JavaScript bloqueado: pulsa **Abrir en pestaña** o abre el archivo en un navegador normal.
4. Si aparece el aviso amarillo **«Estás viendo la página sin JavaScript»**, ocurre lo mismo: el visor no ejecuta scripts.

## Interacciones

- Menú fijo con progreso de lectura y sección activa.
- Botón **Traducción ON/OFF** (global y en la sección de Lope).
- Simulador con presets: *Edipo rey*, *Fuenteovejuna*, *La vida es sueño* y una serie de ocho temporadas.
- Plano del corral con zonas clicables y botones equivalentes (accesibles por teclado).
- Quiz autoevaluable con retroalimentación por pregunta y mensaje final.
- Impresión con estilos específicos.

## Editar

Las fuentes están en `src/`:

- `styles.css`: sistema visual completo.
- `body-1.html` … `body-5.html`: contenido y estructura.
- `app.js`: simulador, corral, quiz, navegación y traducciones.

Después de editar, regenera el archivo final:

```bash
python3 build.py
```

## Criterio y fuentes

- Antonio Sobejano-Morán, *A Guide to the Interpretation of Literary Texts*, Panda Publications, 2017, pp. 466–469 y 506 (definición de las tres unidades y del corral).
- Aristóteles, *Poética*, 1449b–1451a.
- Lope de Vega, *Arte nuevo de hacer comedias en este tiempo*, 1609 (texto de Wikisource; ed. de Juan Manuel Rozas en la Biblioteca Virtual Miguel de Cervantes).
- Lodovico Castelvetro, *Poetica d'Aristotele vulgarizzata e sposta*, 1570; Nicolas Boileau, *Art poétique*, 1674.
- José María Díez Borque, *Teatro del Siglo de Oro: corrales y coliseos en la península ibérica*, Cuadernos de Teatro Clásico, 6, 1991.

Las citas de Lope se mantienen en su forma original; las traducciones “En claro” son adaptaciones didácticas. Los diagramas son SVG originales y no reproducen un corral exacto: son esquemas para pensar.

## Nota de diseño

La pieza alterna papel y tinta, serif editorial y tipografía mono para los datos, con un tono contemporáneo (simulador, chat, quiz) sin sacrificar el rigor conceptual. La idea central que ordena todo: **la comedia nueva no es caos; es otro sistema de reglas**.
