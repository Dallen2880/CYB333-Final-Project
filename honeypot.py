import socket
import datetime
import requests
import winsound
import smtplib
from collections import defaultdict
from email.mime.text import MIMEText

# === BASIC CONFIGURATION ===

HOST = '0.0.0.0'             # Listen on all available interfaces
PORT = 2323                  # Decoy port
LOGFILE = f"honeypot_log_{datetime.date.today()}.txt"  # Log file per day

# === EMAIL CONFIGURATION (Gmail) ===

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FROM = "dustin2880@gmail.com"
EMAIL_TO = "dustin2880@gmail.com"
EMAIL_PASSWORD = "ikmrfqhfttkurzla "  # ← Replace this!
EMAIL_SUBJECT = "⚠️ Honeypot Alert Triggered"

# === TRACK IP CONNECTIONS ===

ip_counter = defaultdict(int)

# === FUNCTION: GEOIP LOOKUP ===
def get_geoip(ip):
    try:
        def get_geoip(ip):
    
         response = requests.get(f"https://ipinfo.io/{ip}/json?token=aca0b4de945a5d", timeout=5)
        data = response.json()
        return f"{data.get('city', 'Unknown')}, {data.get('region', 'Unknown')}, {data.get('country', 'Unknown')}"
    except Exception as e:
        print(f"[X] IPInfo GeoIP error for {ip}: {e}")
        return "GeoIP error"
       
# === FUNCTION: SEND EMAIL ===
def send_email(body):
    msg = MIMEText(body)
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)
            print("[+] Email alert sent.")
    except Exception as e:
        print(f"[X] Failed to send email: {e}")

# === FUNCTION: RUN THE HONEYPOT ===
def run_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Honeypot listening on port {PORT}...\n")

        while True:
            conn, addr = s.accept()
            with conn:
                ip = addr[0]
                timestamp = datetime.datetime.now().isoformat()
                ip_counter[ip] += 1

                # Skip GeoIP for localhost addresses
                if ip.startswith("127."):
                    location = "Localhost (no GeoIP)"
                else:
                    location = get_geoip(ip)

                # Log entry formatting
                log_line = (
                    f"[!] Hit #{ip_counter[ip]} from {ip} "
                    f"({location}) at {timestamp}\n"
                )

                print(log_line.strip())                         # Print to terminal
                with open(LOGFILE, "a") as f:
                    f.write(log_line)                           # Write to log file
                send_email(log_line)                            # Email alert

                winsound.Beep(950, 150)                          # Basic beep
                if ip_counter[ip] > 1:
                    winsound.Beep(1300, 300)                    # Repeat hit = louder

                conn.sendall(b"SSH-2.0-OpenSSH_8.2\r\n")        # Fake SSH banner

# === EXECUTE SCRIPT ===
if __name__ == "__main__":
    run_honeypot()
