# API de Predicción del Rendimiento Académico

## Cómo ejecutar localmente
1. Entrena el modelo:
   ```bash
   python train_model.py
   ```

2. Ejecuta la API:
   ```bash
   python app.py
   ```

## Ejemplo de uso
### Endpoint
POST /predict

### Body (JSON)
```json
{
  "horas_estudio": 12,
  "asistencia": 90,
  "participacion": 8
}
```

### Respuesta
```json
{
  "promedio_predicho": 16.4
}
```

## Ejecutar con Docker
```bash
docker build -t rendimiento_estudiantil .
docker run -p 5000:5000 rendimiento_estudiantil
```
