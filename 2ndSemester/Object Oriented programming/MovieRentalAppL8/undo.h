//
// Created by popla on 24-Apr-25.
//

#ifndef UNDO_H
#define UNDO_H
#include "movie.h"
#include "repository.h"

class UndoAction {
  public:
    virtual void doUndo() = 0;
    virtual ~UndoAction() = default;
};

class AddUndo : public UndoAction {
  private:
    Movie movie_;
    MovieRepository& repo;
  public:
    AddUndo(const Movie& movie, MovieRepository& repo) : movie_{movie}, repo{repo} {}
    void doUndo() override {
      repo.deleteMovie(repo.findPosition(movie_.getTitle()));
    }
};

class DeleteUndo : public UndoAction {
  private:
    Movie movie_;
    MovieRepository& repo;
  public:
    DeleteUndo(const Movie& movie, MovieRepository& repo) : movie_{movie}, repo{repo} {}
    void doUndo() override {
      repo.addMovie(movie_);
    }
};

class UpdateUndo : public UndoAction {
  private:
    Movie movie_;
    MovieRepository& repo;
  public:
    UpdateUndo(const Movie& movie, MovieRepository& repo) : movie_{movie}, repo{repo} {}
    void doUndo() override {
      repo.deleteMovie(repo.findPosition(movie_.getTitle()));
      repo.addMovie(movie_);
    }
};

#endif //UNDO_H
