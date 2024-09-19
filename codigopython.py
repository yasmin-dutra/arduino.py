import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Configuração da porta serial (ajuste o 'COM3' para a porta correta no seu sistema)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Espera o Arduino iniciar a comunicação serial

# Configuração inicial da plotagem
fig, ax = plt.subplots()
x_data, y_data = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(10, 40)
    return ln,

def update(frame):
    try:
        # Lê os dados do Arduino
        data = ser.readline().decode('utf-8').strip()
        if data:
            temperatura = float(data)
            x_data.append(len(x_data))
            y_data.append(temperatura)
            ln.set_data(x_data, y_data)
            if len(x_data) > 100:
                ax.set_xlim(len(x_data) - 100, len(x_data))
            return ln,
    except:
        pass

ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, interval=1000)
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.title('Monitoramento de Temperatura em Tempo Real')
plt.show()

# Fecha a comunicação serial ao terminar
ser.close()