#include <chrono>
#include <iomanip>
#include <memory>
#include <sstream>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class StatusPublisher : public rclcpp::Node {
public:
  StatusPublisher() : Node("status_publisher") {
    publisher_ = create_publisher<std_msgs::msg::String>("/robot/status", 10);
    timer_ = create_wall_timer(500ms, [this]() { publishStatus(); });
  }

private:
  void publishStatus() {
    battery_ -= 0.2;
    if (battery_ < 0.0) {
      battery_ = 100.0;
    }

    temperature_ += temperature_step_;
    if (temperature_ > 45.0 || temperature_ < 34.0) {
      temperature_step_ = -temperature_step_;
    }

    std::ostringstream payload;
    payload << std::fixed << std::setprecision(2)
            << "battery=" << battery_
            << ",temperature=" << temperature_
            << ",velocity=" << velocity_;

    std_msgs::msg::String message;
    message.data = payload.str();
    publisher_->publish(message);
  }

  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
  double battery_{100.0};
  double temperature_{36.5};
  double temperature_step_{0.15};
  double velocity_{0.42};
};

int main(int argc, char **argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<StatusPublisher>());
  rclcpp::shutdown();
  return 0;
}

