#include <iostream>
#include <string>

std::string vowels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

std::string perany(int num, int calsys) {
  std::string res;
  while(num > 0) {
    std::string digit = std::to_string(num%calsys);
    if (num%calsys >= 10) {
  digit = vowels[std::stoi(digit) - 10];
        }
    res = digit + res;
    num /= calsys;
      }
  return res;
    }


int main() {
  int num;
  int calsys;
  std::cout << "enter: num" << std::endl;
  std::cin >> num;
  std::cout << "enter: number system" << std::endl;
  std::cin >> calsys;
  std::cout << perany(num, calsys) << std::endl;
}
