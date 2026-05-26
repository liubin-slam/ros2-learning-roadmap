#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_srvs/srv/trigger.hpp"

class ResetAlarmServer : public rclcpp::Node {
public:
  ResetAlarmServer() : Node("reset_alarm_server") {
    service_ = create_service<std_srvs::srv::Trigger>(
        "/reset_alarm",
        [this](const std::shared_ptr<std_srvs::srv::Trigger::Request>,
               std::shared_ptr<std_srvs::srv::Trigger::Response> response) {
          RCLCPP_INFO(get_logger(), "alarm reset requested");
          response->success = true;
          response->message = "alarm state reset";
        });
  }

private:
  rclcpp::Service<std_srvs::srv::Trigger>::SharedPtr service_;
};

int main(int argc, char **argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ResetAlarmServer>());
  rclcpp::shutdown();
  return 0;
}

