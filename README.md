# Proyecto_Final
## Tenda Virtual
### Joc de compra i venda
## **Descripció del programa:**
Desenvolupar un codi el qual implementi tot el vist a la unitat de “Fem de profes” i que permeti crear un joc/programa sobre una tenda virtual.
##### 1. Interfície de tenda:
  - Crear una interfície que permeti a l'usuari accedir a diferents menús per a la compra d’objectes, la seva venda o altres opcions dintre d’una tenda.
##### 2. Inventari jugador:
  - Crear una interfície que mostri quins objectes té el jugador, per quins preus els ha comprat, i quina quantitat té de cada un.
##### 3. Economia del jugador:
  - El jugador començarà amb una quantitat establerta de doblers per poder començar a comprar. Per guanyar més doblers s’hauran de vendre productes una vegada hagin augmentat de valor.
##### 4. Inventari de Productes:
  - El programa mantindrà un inventari de productes amb detalls com a nom, descripció, preu actual i quantitat disponible.
##### 5. Compra i Venda de Productes:
  - El jugador pot comprar productes disponibles a la botiga. També podran vendre productes que ja hagin comprat amb un increment o decreixement de preu, simulant la compra i venda de producte a la vida real.
##### 6. Fluctuació de Preus:
  - Implementar un sistema on els preus dels productes canviïn basats en l'oferta i la demanda simulada.
##### 7. Notificacions:
  - Avisar als usuaris sobre canvis en els preus dels productes en què estan interessats.

**Material relacionat amb la unitat: Fem de profes.**
- Base de dades: Utilitzar la base de dades SQLite per emmagatzemar informació d’inventaris, productes, transaccions, etc.
- Interfície d'usuari: Crear una interfície d'usuari intuïtiva usant biblioteques com Tkinter o PyQt per mostrar la tenda, l’inventari de l’usuari, etcètera.
- Orientació a objectes: Crear classes per a diferents tipus d’objectes.
- Maneig de Sessions (GitHub): Implementar un sistema de gestió de sessions per controlar l'accés dels usuaris a les funcions del programa. A més, documentar el codi adequadament perquè altres desenvolupadors puguin entendre i modificar el programa si cal per poder fer feina en equip. Escenari d'Ús:
  - L’usuari explora els productes disponibles i decideix comprar-ne un.
  - Fa una compra i el preu del producte s'ajusta segons la fluctuació de preus.
  - Els canvis es van acumulant a la tenda fins que hi hagi un ecosistema establert d’oferta i demanda.
  - Els usuaris poden veure l‘historial de transaccions i rebre notificacions sobre canvis de preus en productes del vostre interès.
