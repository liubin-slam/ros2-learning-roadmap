import random
import time


def main():
    while True:
        timestamp_ms = int(time.time() * 1000)
        ax = random.uniform(-0.05, 0.05)
        ay = random.uniform(-0.05, 0.05)
        az = 9.81 + random.uniform(-0.08, 0.08)
        gx = random.uniform(-0.003, 0.003)
        gy = random.uniform(-0.003, 0.003)
        gz = random.uniform(-0.003, 0.003)
        print(f"{timestamp_ms},{ax:.4f},{ay:.4f},{az:.4f},{gx:.5f},{gy:.5f},{gz:.5f}", flush=True)
        time.sleep(0.01)


if __name__ == "__main__":
    main()

