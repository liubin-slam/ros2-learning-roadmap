#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class StatusMonitor : public rclcpp::Node {
public:
  StatusMonitor() : Node("status_monitor") {
    declare_parameter("min_battery_percent", 20.0);
    declare_parameter("max_temperature_c", 42.0);

    min_battery_ = get_parameter("min_battery_percent").as_double();
    max_temperature_ = get_parameter("max_temperature_c").as_double();

    subscription_ = create_subscription<std_msgs::msg::String>(
        "/robot/status", 10,
        [this](const std_msgs::msg::String::SharedPtr message) {
          inspect(message->data);
        });
  }

private:
  static double readValue(const std::string &text, const std::string &key) {
    const auto pos = text.find(key + "=");
    if (pos == std::string::npos) {
      return 0.0;
    }
    const auto start = pos + key.size() + 1;
    const auto end = text.find(',', start);
    return std::stod(text.substr(start, end - start));
  }

  void inspect(const std::string &status) {
    const double battery = readValue(status, "battery");
    const double temperature = readValue(status, "temperature");

    if (battery < min_battery_) {
      RCLCPP_WARN(get_logger(), "low battery: %.2f%%", battery);
    }
    if (temperature > max_temperature_) {
      RCLCPP_WARN(get_logger(), "high temperature: %.2fC", temperature);
    }
  }

  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
  double min_battery_{20.0};
  double max_temperature_{42.0};
};

int main(int argc, char **argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<StatusMonitor>());
  rclcpp::shutdown();
  return 0;
}

