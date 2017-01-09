/*
 * Challenge I1
 * https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/
 */

#include <iostream>
#include <vector>

int main() {
    bool running = true;
    int hour;
    int choice;
    std::vector<std::string> appointments(24, "Nothing scheduled.");

    std::cout << "Hello! Welcome to the 24H calendar!" << std::endl;
    while (running){
        std::cout << "What would you like to do?" << std::endl;
        std::cout << "1. View Calender" << std::endl <<
                "2. Add/Change Appointment" << std::endl <<
                "3. Remove Appointment" << std::endl <<
                "4. Exit" << std::endl;
        std::cout << "Enter the choice: ";
        std::cin >> choice;
        if (choice == 1){
            std::cout << std::endl << "24H Calendar" << std::endl;
            for (int i = 0; i < appointments.size(); ++i){
                std::cout << i << " : " << appointments[i] << std::endl;
            }
            std::cout << std::endl;
        }
        else if (choice == 2){
            std::cout << "What hour would you like to add/change? ";
            std::cin >> hour;
            std::cout << std::endl << "What is the description?" << std::endl;
            std::cin >> appointments[hour];
            std::cout << std::endl;
        }
        else if (choice == 3){
            std::cout << "What hour would you like to remove? ";
            std::cin >> hour;
            appointments[hour] = "Nothing scheduled.";
            std::cout << std::endl;
        }
        else if (choice == 4){
            running = false;
            std::cout << "Goodbye." << std::endl;
        }
        else {
            std::cout << "Choice invalid." << std::endl << std::endl;
        }
    }
    return 0;
}