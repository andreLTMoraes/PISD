import tensorflow as tf
import numpy as np
import paho.mqtt.client as mqtt
import time
import json

x = np.array([[0.1], [0.2], [0.3], [0.4]], dtype=np.float32)
y = np.array([[0], [0], [1], [1]], dtype=np.float32)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, activation='sigmoid', input_shape=(1,))
])
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(x, y, epochs=100, verbose=0)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("modelo.tflite", "wb") as f:
    f.write(tflite_model)

interpreter = tf.lite.Interpreter(model_path="modelo.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

THINGSBOARD_HOST = "http://localhost"
ACCESS_TOKEN = "asdfkjewoisdnnweiurwyhaoeif87j"

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

print("Enviando dados a cada 5 segundos. Pressione Ctrl+C para parar.")

try:
    while True:
        entrada_simulada = np.random.uniform(0.0, 0.5)
        entrada = np.array([[entrada_simulada]], dtype=np.float32)

        interpreter.set_tensor(input_details[0]['index'], entrada)
        interpreter.invoke()
        saida = interpreter.get_tensor(output_details[0]['index'])
        resultado = float(saida[0][0])

        payload = {
            "entrada_simulada": round(entrada_simulada, 4),
            "resultado_modelo": round(resultado, 4)
        }

        client.publish("v1/devices/me/telemetry", json.dumps(payload))
        print("Enviado:", payload)

        time.sleep(5)

except KeyboardInterrupt:
    print("\nInterrompido pelo usuário.")
    client.loop_stop()
    client.disconnect()