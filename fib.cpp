#include <iostream>
#include <chrono>
#include <unordered_map>

long long unsigned int fib(int n) {
    static std::unordered_map<int, long long unsigned> cache; //словарь 
    if (n <= 1) return n;
    if (cache.find(n) != cache.end()) return cache[n];

    unsigned long long result = fib(n - 1) + fib(n - 2);

    cache.emplace(n, result);
    return result;
}

int main() {
    int num;
    long long unsigned int xd;
    bool going = true;
    while (going) {
        std::cout << "enter num for find fib: ";
        std::cin >> num;
        auto start = std::chrono::high_resolution_clock::now();
        xd = fib(num);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> duration = end - start;
        std::cout << "Calculation time: " << duration.count() << std::endl;
        std::cout << xd << std::endl;
    }
}
