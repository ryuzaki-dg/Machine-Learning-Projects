#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// Structure to store a task
struct Task {
    string description;
    bool isCompleted;
};

// Function prototypes
void loadTasks(vector<Task>& tasks, const string& filename);
void saveTasks(const vector<Task>& tasks, const string& filename);
void addTask(vector<Task>& tasks);
void showTasks(const vector<Task>& tasks);
void markCompleted(vector<Task>& tasks);
void deleteTask(vector<Task>& tasks);

int main() {
    vector<Task> tasks;
    string filename = "tasks.txt";
    int choice;

    loadTasks(tasks, filename);

    do {
        cout << "\n------ To-Do List ------\n";
        cout << "1. Add Task\n";
        cout << "2. Show Tasks\n";
        cout << "3. Mark Task as Completed\n";
        cout << "4. Delete Task\n";
        cout << "0. Exit\n";
        cout << "------------------------\n";
        cout << "Enter your choice: ";
        cin >> choice;
        cin.ignore();

        switch (choice) {
        case 1:
            addTask(tasks);
            break;
        case 2:
            showTasks(tasks);
            break;
        case 3:
            markCompleted(tasks);
            break;
        case 4:
            deleteTask(tasks);
            break;
        case 0:
            saveTasks(tasks, filename);
            cout << "Tasks saved. Exiting...\n";
            break;
        default:
            cout << "Invalid choice. Try again.\n";
        }

    } while (choice != 0);

    return 0;
}

// Load tasks from file
void loadTasks(vector<Task>& tasks, const string& filename) {
    ifstream inFile(filename);
    if (!inFile) return;

    Task task;
    string status;

    while (getline(inFile, task.description)) {
        getline(inFile, status);
        task.isCompleted = (status == "1");
        tasks.push_back(task);
    }

    inFile.close();
}

// Save tasks to file
void saveTasks(const vector<Task>& tasks, const string& filename) {
    ofstream outFile(filename);

    for (const auto& task : tasks) {
        outFile << task.description << endl;
        outFile << (task.isCompleted ? "1" : "0") << endl;
    }

    outFile.close();
}

// Add a task
void addTask(vector<Task>& tasks) {
    Task task;
    cout << "Enter task description: ";
    getline(cin, task.description);
    task.isCompleted = false;
    tasks.push_back(task);
    cout << "Task added!\n";
}

// Display all tasks
void showTasks(const vector<Task>& tasks) {
    if (tasks.empty()) {
        cout << "No tasks to display.\n";
        return;
    }

    cout << "\n--- To-Do List ---\n";
    for (size_t i = 0; i < tasks.size(); ++i) {
        cout << i + 1 << ". [" << (tasks[i].isCompleted ? "X" : " ") << "] "
            << tasks[i].description << endl;
    }
}

// Mark a task as completed
void markCompleted(vector<Task>& tasks) {
    int index;
    showTasks(tasks);

    cout << "Enter task number to mark as completed: ";
    cin >> index;
    cin.ignore();

    if (index < 1 || index > tasks.size()) {
        cout << "Invalid task number.\n";
    }
    else {
        tasks[index - 1].isCompleted = true;
        cout << "Task marked as completed.\n";
    }
}

// Delete a task
void deleteTask(vector<Task>& tasks) {
    int index;
    showTasks(tasks);

    cout << "Enter task number to delete: ";
    cin >> index;
    cin.ignore();

    if (index < 1 || index > tasks.size()) {
        cout << "Invalid task number.\n";
    }
    else {
        tasks.erase(tasks.begin() + index - 1);
        cout << "Task deleted.\n";
    }
}
