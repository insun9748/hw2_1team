#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <thread> 
#include <chrono>
#include <windows.h>

using namespace std;


void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void display(const vector<string>& stack, string action) {
    clearScreen();
    cout << "--- " << action << " ---" << endl << endl;
    cout << "[ Stack Status ]" << endl;

    // 스택 크기 10 이하
    for (int i = 9; i >= 0; i--) {
        if (i < stack.size())
            cout << "| " << stack[i] << " |" << endl;
        else
            cout << "|            |" << endl;
    }
    cout << "--------------" << endl;
    this_thread::sleep_for(chrono::milliseconds(800)); 
}

int main() {
    system("chcp 65001");

    vector<string> stack; 
    vector<string> words;
    ifstream file("HW2.csv");
    string line;

    // CSV 파일 읽기
    while (getline(file, line)) {
        stringstream ss(line);
        string item;
        int col = 0;
        while (getline(ss, item, ',')) {
            if (col >= 2) words.push_back(item); 
            col++;
        }
    }

    // 스택 연산 애니메이션
    for (const string& w : words) {
        if (stack.size() >= 10) { 
            stack.pop_back();
            display(stack, "stack.pop()");
        }

        stack.push_back(w); //push 연산
        display(stack, "stack.push(\"" + w + "\")");
    }

    //top 연산
    if (!stack.empty()) {
        display(stack, "stack.top() -> " + stack.back());
    }

   //pop 연산 
    stack.pop_back();
    display(stack, "stack.pop()");

    cout << "\ncompleted" << endl;
    return 0;
}