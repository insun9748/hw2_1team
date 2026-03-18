#include <iostream>
#include <stack>     
#include <vector>
#include <string>
#include <thread>     
#include <chrono>

using namespace std;

void refresh(const stack<string>& s, string command) {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif

    cout << "----------------------------------------" << endl;
    cout << " [현재 연산]: " << command << endl;
    cout << "----------------------------------------" << endl << endl;

    stack<string> temp = s;
    vector<string> items;
    while (!temp.empty()) {
        items.push_back(temp.top());
        temp.pop();
    }

    if (items.empty()) {
        cout << "  [ EMPTY ]" << endl;
    }
    else {
        for (int i = 0; i < items.size(); ++i) {
            cout << "  |  " << items[i] << (i == 0 ? "  | <-- TOP" : "  |") << endl;
            cout << "----------------" << endl;
        }
    }
    cout << "  [  STACK  ]  " << endl << endl;

    this_thread::sleep_for(chrono::milliseconds(1500));
}

int main() {
    vector<string> data = {
        "산책", "드립커피", "우드",
        "꽃놀이", "핑크", "개강",
        "개나리", "중간고사", "스타벅스",
        "수플레", "라떼", "가로수",
        "나들이", "한강", "차",
        "커피", "향기", "민들레"
    };

    stack<string> s;
    refresh(s, "stack<string> s");

    for (int i = 0; i < data.size(); ++i) {

        if (s.size() >= 8) {
            string topVal = s.top(); 
            refresh(s, "s.top() // 현재 최상단은 " + topVal);

            s.pop(); 
            refresh(s, "s.pop()");
        }

        s.push(data[i]);
        refresh(s, "s.push(\"" + data[i] + "\")");
    }

    cout << "모든 팀원 단어 처리 완료!" << endl;
    return 0;
}