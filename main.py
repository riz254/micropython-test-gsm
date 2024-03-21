
from machine import UART
import time

# Function to initialize UART communication
def init_uart(tx_pin, rx_pin, baud_rate):
    return UART(1, baud_rate, tx=tx_pin, rx=rx_pin)

# Function to send AT command and read response
def send_at_command(uart, command, timeout=1000):
    uart.write(command + b'\r\n')
    time.sleep_ms(timeout)
    return uart.read()

def check_signal_strength(uart):
    uart.write(b'AT+CSQ\r\n')  # Command to check signal strength
    response = uart.read()
    print("Signal Strength Response:", response)

def check_network_registration(uart):
    uart.write(b'AT+CREG?\r\n')  # Command to check network registration status
    response = uart.read()
    print("Network Registration Response:", response)

# Function to send SMS
def send_sms(uart, recipient_number, message):
    uart.write('AT+CMGF=1\r\n')  # Set SMS text mode
    time.sleep_ms(500)
    uart.write('AT+CMGS="{}"\r\n'.format(recipient_number))
    time.sleep_ms(500)
    uart.write(message + '\x1A')
    time.sleep_ms(500)

if __name__ == "__main__":
    # Configure UART pins and baud rate
    TX_PIN = 17  # Replace with your TX pin
    RX_PIN = 16  # Replace with your RX pin
    BAUD_RATE = 9600  # Baud rate of your GSM module

    # Initialize UART
    uart = init_uart(TX_PIN, RX_PIN, BAUD_RATE)

    # Wait for the module to be ready
    time.sleep(2)

    # Send AT command to check if module is responsive
    response = send_at_command(uart, b'AT')
    print(response)

    # Set recipient number and message
    recipient_number = "0792386531"  # Replace with recipient's number
    message = "Hello, this is a test message from GSM modem!"

    # Send SMS
    send_sms(uart, recipient_number, message)

    check_signal_strength(uart)
    check_network_registration(uart)
