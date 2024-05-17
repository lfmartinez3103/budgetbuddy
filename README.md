# budgetbuddy

Este proyecto es una aplicación para mostrar información de presupuestos de viajes.

## Instalación

Para configurar y ejecutar este proyecto, sigue estos pasos:

1. Clona el repositorio:

```bash
git clone https://github.com/lfmartinez3103/budgetbuddy
```

2. Navega al directorio del proyecto:

```bash
cd budgetbuddy
```

3. Crea el entorno virtual
```bash
python -m venv venv
```

4. Activa el entorno virtual
```bash
venv\Scripts\activate
```

5. Instala las dependencias
```bash
pip install -r requirements.txt
```

6. Crea un archivo con el nombre `.env` y agrega los siguientes datos.
```bash
APP_NAME=BudgetBuddy
BG_COLOR=395173
LOGO_COLOR_YELLOW=ffbd54
```

## Testear en aplicacion de flet

```bash
flet run --android
```

Copias la url y la agregas en la aplicacion o escanea el QR

**NOTA:** Recuerda que cada vez que vas a testearlo el celular y el computador deben estar en la misma red de internet
