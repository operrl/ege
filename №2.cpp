#include <iostream>

int main() 
{ 
  for (int i = 0; i <= 1; i++){
    std::cout << "F = " << i << std::endl;
    std::cout << "x " << "y " << "w " << "z " << std::endl; 
    for (int x = 0; x <= 1; x++){
      for (int y = 0; y <= 1; y++){
        for (int w = 0; w <= 1; w++){
          for (int z = 0; z <= 1; z++){
              //сюда любое условие// 
              std::cout << x << ' ' << y << ' ' << w << ' ' << z << std::endl;
            }
          }
        }
      }
    }
  }
    return 0;
}
