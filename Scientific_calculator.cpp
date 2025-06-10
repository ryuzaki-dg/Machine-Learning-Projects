#include <iostream>
#include <limits>
#define _USE_MATH_DEFINES
#include <cmath>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif


using namespace std;

// Function prototypes
void displayMenu();
void performOperation(int choice);
long long factorial(int n);

int main() {
    int choice;

    do {
        displayMenu();
        cout << "Enter your choice (0 to exit): ";
        cin >> choice;

        if (cin.fail()) {
            cout << "Invalid input. Exiting.\n";
            break;
        }

        if (choice != 0) {
            performOperation(choice);
        }

    } while (choice != 0);

    cout << "Exiting Scientific Calculator. Goodbye!" << endl;
    return 0;
}

// Function to display menu
void displayMenu() {
    cout << "\n------ Scientific Calculator ------\n";
    cout << "1. Addition\n";
    cout << "2. Subtraction\n";
    cout << "3. Multiplication\n";
    cout << "4. Division\n";
    cout << "5. Power (x^y)\n";
    cout << "6. Square Root\n";
    cout << "7. Sine\n";
    cout << "8. Cosine\n";
    cout << "9. Tangent\n";
    cout << "10. Logarithm (base 10)\n";
    cout << "11. Natural Logarithm (ln)\n";
    cout << "12. Factorial\n";
    cout << "0. Exit\n";
    cout << "----------------------------------\n";
}

// Function to perform chosen operation
void performOperation(int choice) {
    double num1, num2, result;

    switch (choice) {
    case 1:
        cout << "Enter two numbers: ";
        cin >> num1 >> num2;
        result = num1 + num2;
        cout << "Result: " << result << endl;
        break;
    case 2:
        cout << "Enter two numbers: ";
        cin >> num1 >> num2;
        result = num1 - num2;
        cout << "Result: " << result << endl;
        break;
    case 3:
        cout << "Enter two numbers: ";
        cin >> num1 >> num2;
        result = num1 * num2;
        cout << "Result: " << result << endl;
        break;
    case 4:
        cout << "Enter two numbers: ";
        cin >> num1 >> num2;
        if (num2 == 0) {
            cout << "Error: Division by zero.\n";
        }
        else {
            result = num1 / num2;
            cout << "Result: " << result << endl;
        }
        break;
    case 5:
        cout << "Enter base and exponent: ";
        cin >> num1 >> num2;
        result = pow(num1, num2);
        cout << "Result: " << result << endl;
        break;
    case 6:
        cout << "Enter a number: ";
        cin >> num1;
        if (num1 < 0) {
            cout << "Error: Cannot take square root of negative number.\n";
        }
        else {
            result = sqrt(num1);
            cout << "Result: " << result << endl;
        }
        break;
    case 7:
        cout << "Enter angle in degrees: ";
        cin >> num1;
        result = sin(num1 * M_PI / 180.0);
        cout << "Result (sine): " << result << endl;
        break;
    case 8:
        cout << "Enter angle in degrees: ";
        cin >> num1;
        result = cos(num1 * M_PI / 180.0);
        cout << "Result (cosine): " << result << endl;
        break;
    case 9:
        cout << "Enter angle in degrees: ";
        cin >> num1;
        result = tan(num1 * M_PI / 180.0);
        cout << "Result (tangent): " << result << endl;
        break;
    case 10:
        cout << "Enter a number: ";
        cin >> num1;
        if (num1 <= 0) {
            cout << "Error: Logarithm undefined for non-positive numbers.\n";
        }
        else {
            result = log10(num1);
            cout << "Result (log base 10): " << result << endl;
        }
        break;
    case 11:
        cout << "Enter a number: ";
        cin >> num1;
        if (num1 <= 0) {
            cout << "Error: Natural log undefined for non-positive numbers.\n";
        }
        else {
            result = log(num1);
            cout << "Result (ln): " << result << endl;
        }
        break;
    case 12:
        int n;
        cout << "Enter a non-negative integer: ";
        cin >> n;
        if (n < 0) {
            cout << "Error: Factorial not defined for negative numbers.\n";
        }
        else {
            cout << "Result: " << factorial(n) << endl;
        }
        break;
    default:
        cout << "Invalid choice.\n";
    }
}

// Recursive function to calculate factorial
long long factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}
