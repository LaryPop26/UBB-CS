//
// Created by popla on 16-Apr-25.
//

#ifndef OBSERVER_H
#define OBSERVER_H

#include <algorithm>
#include <vector>
using std::vector;

class Observer {
public:
virtual ~Observer() = default;
  virtual void update() = 0;
};

class Observable {
private:
  vector<Observer*> observers;

public:

  void addObserver(Observer* observer) {
    observers.push_back(observer);
  }

  void deleteObserver(Observer* observer) {
    observers.erase(remove(observers.begin(),observers.end(), observer), observers.end());
  }

  void notify() const {
    for (auto *observer: observers) {
      observer->update();
    }
  }
 };

#endif //OBSERVER_H
