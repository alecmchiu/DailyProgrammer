/*
 * Challenge H2
 * https://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/
 */

#include <iostream>

int main() {
    std::cout << "Stopwatch" << std::endl;
    std::cout << "l = lap; q = quit" << std::endl;
    std::cout << "Enter 's' to start" << std::endl;

    std::time_t start;

    char choice;
    std::cin >> choice;

    if (choice == 's'){
        start = std::time(NULL);
    }
    else {
        std::cout << "Invalid choice. Exiting." << std::endl;
        return 0;
    }

    std::time_t last = start;

    while (choice != 'q'){
        std::cin >> choice;
        if (choice == 'l') {
            std::cout << std::time(NULL) - last << " seconds" << std::endl;
            last = std::time(NULL);
        }
    }

    std::cout << "Ran for " << std::time(NULL) - start << " seconds" << std::endl;

    std::cout << "Goodbye." << std::endl;

    return 0;
}