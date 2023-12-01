from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo para 20 lugares de Airbnb
datos_airbnb = [
  {
    "codigo": "L001",
    "nombre": "Machu Picchu",
    "precio": 150,
    "ubicacion": "Cusco",
    "detalle": "Antigua ciudad inca",
    "imagenes": ["url_machu_picchu_1.jpg", "url_machu_picchu_2.jpg"]
  },
  {
    "codigo": "L002",
    "nombre": "Lago Titicaca",
    "precio": 120,
    "ubicacion": "Puno",
    "detalle": "Lago navegable más alto del mundo",
    "imagenes": ["url_lago_titicaca_1.jpg", "url_lago_titicaca_2.jpg"]
  },
   {
    "codigo": "L003",
    "nombre": "Catedral de Lima",
    "precio": 50,
    "ubicacion": "Lima",
    "detalle": "Impresionante catedral en el centro histórico",
    "imagenes": ["url_catedral_lima_1.jpg", "url_catedral_lima_2.jpg"]
  },
  {
    "codigo": "L004",
    "nombre": "Colca Canyon",
    "precio": 90,
    "ubicacion": "Arequipa",
    "detalle": "Cañón más profundo del mundo",
    "imagenes": ["url_colca_canyon_1.jpg", "url_colca_canyon_2.jpg"]
  },
  {
    "codigo": "L005",
    "nombre": "Montañas Rainbow (Vinicunca)",
    "precio": 80,
    "ubicacion": "Cusco",
    "detalle": "Montañas con colores vibrantes",
    "imagenes": ["url_montanas_rainbow_1.jpg", "url_montanas_rainbow_2.jpg"]
  },
  {
    "codigo": "L006",
    "nombre": "Trujillo",
    "precio": 70,
    "ubicacion": "La Libertad",
    "detalle": "Ciudad con impresionantes ruinas arqueológicas",
    "imagenes": ["url_trujillo_1.jpg", "url_trujillo_2.jpg"]
  },
  {
    "codigo": "L007",
    "nombre": "Amazonía Peruana",
    "precio": 200,
    "ubicacion": "Iquitos",
    "detalle": "Explora la rica biodiversidad de la Amazonía",
    "imagenes": ["url_amazonia_peruana_1.jpg", "url_amazonia_peruana_2.jpg"]
  },
  {
    "codigo": "L008",
    "nombre": "Chan Chan",
    "precio": 60,
    "ubicacion": "Trujillo",
    "detalle": "Ciudadela de barro más grande de América",
    "imagenes": ["url_chan_chan_1.jpg", "url_chan_chan_2.jpg"]
  },
  {
    "codigo": "L009",
    "nombre": "Islas Ballestas",
    "precio": 70,
    "ubicacion": "Ica",
    "detalle": "Islas llenas de vida marina y aves",
    "imagenes": ["url_islas_ballestas_1.jpg", "url_islas_ballestas_2.jpg"]
  },
  {
    "codigo": "L010",
    "nombre": "Reserva Nacional de Paracas",
    "precio": 80,
    "ubicacion": "Ica",
    "detalle": "Área de conservación con paisajes impresionantes",
    "imagenes": ["url_paracas_1.jpg", "url_paracas_2.jpg"]
  },
  {
    "codigo": "L011",
    "nombre": "Máncora",
    "precio": 90,
    "ubicacion": "Piura",
    "detalle": "Playa famosa por sus olas y vida nocturna",
    "imagenes": ["url_mancora_1.jpg", "url_mancora_2.jpg"]
  },
  {
    "codigo": "L012",
    "nombre": "Cascadas de Gocta",
    "precio": 100,
    "ubicacion": "Amazonas",
    "detalle": "Una de las cascadas más altas del mundo",
    "imagenes": ["url_gocta_1.jpg", "url_gocta_2.jpg"]
  },
  {
    "codigo": "L013",
    "nombre": "Centro Histórico de Arequipa",
    "precio": 75,
    "ubicacion": "Arequipa",
    "detalle": "Arquitectura colonial y vistas panorámicas",
    "imagenes": ["url_centro_historico_arequipa_1.jpg", "url_centro_historico_arequipa_2.jpg"]
  },
  {
    "codigo": "L014",
    "nombre": "Huaca Pucllana",
    "precio": 55,
    "ubicacion": "Lima",
    "detalle": "Sitio arqueológico en medio de la ciudad",
    "imagenes": ["url_huaca_pucllana_1.jpg", "url_huaca_pucllana_2.jpg"]
  },
  {
    "codigo": "L015",
    "nombre": "Pacaya Samiria",
    "precio": 180,
    "ubicacion": "Loreto",
    "detalle": "Reserva natural en la Amazonía",
    "imagenes": ["url_pacaya_samiria_1.jpg", "url_pacaya_samiria_2.jpg"]
  },
  {
    "codigo": "L016",
    "nombre": "Moray",
    "precio": 65,
    "ubicacion": "Cusco",
    "detalle": "Terrazas agrícolas incas",
    "imagenes": ["url_moray_1.jpg", "url_moray_2.jpg"]
  },
  {
    "codigo": "L017",
    "nombre": "Playa Roja",
    "precio": 70,
    "ubicacion": "Ica",
    "detalle": "Playa con arena de tonalidad rojiza",
    "imagenes": ["url_playa_roja_1.jpg", "url_playa_roja_2.jpg"]
  },
   {
    "codigo": "L018",
    "nombre": "Líneas de Nazca",
    "precio": 95,
    "ubicacion": "Ica",
    "detalle": "Misteriosas geoglifos en el desierto",
    "imagenes": ["url_lineas_nazca_1.jpg", "url_lineas_nazca_2.jpg"]
  },
  
  {
    "codigo": "L019",
    "nombre": "Parque Nacional Huascarán",
    "precio": 80,
    "ubicacion": "Áncash",
    "detalle": "Reserva de la biosfera y parque nacional",
    "imagenes": ["url_parque_huascaran_1.jpg", "url_parque_huascaran_2.jpg"]
  },
  {
    "codigo": "L020",
    "nombre": "Arequipa",
    "precio": 100,
    "ubicacion": "Arequipa",
    "detalle": "Ciudad rodeada de volcanes",
    "imagenes": ["url_arequipa_1.jpg", "url_arequipa_2.jpg"]
  }
]



@app.route('/api/lugares', methods=['GET'])
def obtener_lugares():
    return jsonify({"lugares": datos_airbnb})

if __name__ == '__main__':
    app.run(debug=True)
