#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <thread>

struct SensorSample {
  long long timestamp_ms;
  double temperature_c;
  double battery_percent;
  double velocity_mps;
};

class SensorSimulator {
public:
  SensorSimulator()
      : rng_(std::random_device{}()),
        temperature_noise_(-0.4, 0.4),
        velocity_noise_(-0.08, 0.08) {}

  SensorSample sample() {
    const auto now = std::chrono::system_clock::now();
    const auto timestamp_ms =
        std::chrono::duration_cast<std::chrono::milliseconds>(
            now.time_since_epoch())
            .count();

    battery_percent_ -= 0.02;
    if (battery_percent_ < 0.0) {
      battery_percent_ = 100.0;
    }

    return SensorSample{
        timestamp_ms,
        36.5 + temperature_noise_(rng_),
        battery_percent_,
        0.5 + velocity_noise_(rng_),
    };
  }

private:
  std::mt19937 rng_;
  std::uniform_real_distribution<double> temperature_noise_;
  std::uniform_real_distribution<double> velocity_noise_;
  double battery_percent_{100.0};
};

class CsvLogger {
public:
  explicit CsvLogger(const std::string &path) : file_(path) {
    if (!file_) {
      throw std::runtime_error("failed to open output file: " + path);
    }
    file_ << "timestamp_ms,temperature_c,battery_percent,velocity_mps\n";
  }

  void write(const SensorSample &sample) {
    file_ << sample.timestamp_ms << ','
          << std::fixed << std::setprecision(2)
          << sample.temperature_c << ','
          << sample.battery_percent << ','
          << sample.velocity_mps << '\n';
  }

private:
  std::ofstream file_;
};

int main() {
  try {
    SensorSimulator simulator;
    CsvLogger logger("sensor_log.csv");

    for (int i = 0; i < 100; ++i) {
      const auto sample = simulator.sample();
      logger.write(sample);

      std::cout << "temperature=" << sample.temperature_c
                << "C battery=" << sample.battery_percent
                << "% velocity=" << sample.velocity_mps << "m/s\n";

      std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
  } catch (const std::exception &error) {
    std::cerr << "error: " << error.what() << '\n';
    return 1;
  }

  return 0;
}

