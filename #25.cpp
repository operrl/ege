#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>


std::vector<int> solve(int num) { //количество делителей числа
    std::vector<int> nums = {}; // массив с делителями
    for (int i = 1; i <= sqrt(num); i++) { // цикл для перебора данных до корня из числа(объясняли на занятии) 
        if ((num % i == 0) && (i * i != num)) { //если число делится нацело и это не корень из числа
            nums.push_back(i); //тогда добавляем его 
            nums.push_back(num / i); //операция по нахождению другого делителя (36 / 2 = 18 => 36 / 18 = 2)
        }
        if ((num % i == 0) && (i * i == num)) { //если число корень, то просто его добавляем
            nums.push_back(i);
        }
    }
    std::sort(nums.begin(), nums.end());
    return nums; //возвращаем ответ
}




int main() {
    std::vector<int> idc = solve(36);
    for (auto i = begin(idc); i != end(idc); ++i) {
        if (i == begin(idc)) {
            std::cout << *i;
        }
        else {
            std::cout << " " << *i;
        }
    }
    return 0;
}
