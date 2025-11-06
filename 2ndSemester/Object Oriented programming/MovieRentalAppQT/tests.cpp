//
// Created by popla on 02-Apr-25.
//

#include "tests.h"
#include "service.h"
#include <cassert>
#include <iostream>
#include <sstream>

#include <fstream>

constexpr int year_1990 = 1990;
constexpr int year_1972 = 1972;
constexpr int year_1993 = 1993;
constexpr int year_1997 = 1997;
constexpr int year_2000 = 2000;
constexpr int year_2003 = 2003;
constexpr int year_2004 = 2004;
constexpr int year_2005 = 2005;
constexpr int number_5 = 5;
constexpr int number_10 = 10;

void testRepo() {
    //MovieRepository repo;
    RepoFile repo("movies-testing.txt");
    // add
    Movie movie1{"Titanic","Action",year_1997, "Leonardo DiCaprio"};
    repo.addMovie(movie1);
    assert(repo.getMovies().size() == 1);

    try {
        repo.addMovie(movie1);
    }
    catch(const RepoException& exp) {
        std::stringstream out;
        out << exp;
        assert(out.str() == "Movie is already in the list");
    }

    // delete
    Movie movie2{"The piano","Drama",year_1993, "Anna Paquin"};
    repo.addMovie(movie2);
    Movie movie3{"Mystic River","Crime", year_2003,"Kevin Bacon"};
    repo.addMovie(movie3);
    assert(repo.getMovies().size() == 3);
    repo.deleteMovie(2);
    assert(repo.getMovies().size() == 2);
    repo.deleteMovie(0);
    assert(repo.getMovies().size() == 1);

    try {
        repo.deleteMovie(-1);
    } catch (const RepoException& e) {
        std::stringstream out;
        out << e;
        assert(out.str() == "Invalid position");
    }

    repo.addMovie(movie1);
    repo.addMovie(movie3);
    assert(repo.getMovies().size() == 3);

    // update
    Movie m4Update{"Mystic River","Thriller", year_2004,"Kevin Bacon"};

    repo.updateMovie(m4Update);
    assert(repo.getMovies().size() == 3);
    assert(m4Update.getGenre()=="Thriller");
    Movie movie5{"Mystic","Thriller", year_2004,"Kevin Bacon"};
    try {
        repo.updateMovie(movie5);
    }
    catch(const RepoException&) {
        assert(true);
    }

    // find position
    const int position = repo.findPosition("Mystic River");
    assert(position == 2);
    try {
        (void)repo.findPosition("Speedy");
    }
    catch(const RepoException&) {
        assert(true);
    }
    try {
        (void)repo.searchMovie("NonExistingMovie");
    } catch (const RepoException& e) {
        std::stringstream out;
        out << e;
        assert(out.str() == "Movie not found");
    }

    std::ofstream clear1("movies-testing.txt", std::ios::trunc);
    clear1.close();
}

void test_read_from_file() {

    try {
        RepoFile repo("mov.txt");
    } catch (const RepoException& e) {
        std::stringstream out;
        out << e;
        assert(out.str() == "File not found");
    }

    std::ofstream fout("movies-test1.txt");
    fout<<"Titanic\n";
    fout<<"Romance\n";
    fout<<"1997\n";
    fout<<"Leonardo DiCaprio\n";

    fout<<"Spider-Man 2\n";
    fout<<"SF\n";
    fout<<"2004\n";
    fout<<"Tobey Maguire\n";
    fout.close();

    RepoFile repo{"movies-test1.txt"};
    assert(repo.getMovies().size() == 2);

    assert(repo.getMovies()[0].getGenre()=="Romance");

    std::ofstream out("movies-test1.txt",std::ios::trunc);
    out.close();
}

void testService() {
    MovieRepository repo;
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};

    // add
    srv.addMovie("Fast&Furious","Action",year_2004,"Vin Diesel");
    srv.addMovie("Titanic","Romance",year_1997,"Leonardo DiCaprio");
    try {
        srv.addMovie("","",number_10,"");
    }
    catch(const ValidationError& exp) {
        std::stringstream out;
        out << exp;
        assert(out.str().find("empty") >= 3);
        assert(out.str().find("correct") >= 1);
    }

    // delete
    assert(srv.getMovies().size() == 2);
    srv.deleteMovie("Titanic");
    assert(srv.getMovies().size() == 1);

    srv.addMovie("Titanic","Romance",year_1997,"Leonardo DiCaprio");

    // update
    srv.updateMovie("Titanic","Comedy",year_2000, "Leo DiCaprio");
    assert(srv.getMovies().size() == 2);

    // find
    const Movie movie = srv.searchMovie("Titanic");
    assert(movie.getGenre()=="Comedy");
    assert(movie.getYear()==2000);
    assert(movie.getMainChar()=="Leo DiCaprio");
}

void testFilterFunctions(const MovieRent & srv) {
  const vector<Movie> filteredGenre = srv.filterGenre("Romance");
    assert(filteredGenre.size() == 3);
    assert(filteredGenre[0].getTitle() == "Titanic");
    assert(filteredGenre[2].getTitle() == "ABCD");

    const vector<Movie> filteredYear = srv.filterYear(year_2000);
    assert(filteredYear.size() == 2);
    assert(filteredYear[0].getTitle() == "ABC");
    assert(filteredYear[1].getTitle() == "ABCD");

    const vector<Movie> filteredYear2 = srv.filterYear(year_1990);
    assert(filteredYear2.empty());
}

void testSortTitle(const MovieRent & srv) {
    const vector<Movie> sortTitleAsc = srv.sorting(SortType::Title, SortOrder::Ascending);
    assert(sortTitleAsc[0].getTitle() == "ABC");
    assert(sortTitleAsc[1].getTitle() == "ABCD");
    assert(sortTitleAsc[2].getTitle() == "Fast&Furious");
    assert(sortTitleAsc[3].getTitle() == "Titanic");
    assert(sortTitleAsc[4].getTitle() == "Yas");

    const vector<Movie> sortTitleDesc = srv.sorting(SortType::Title, SortOrder::Descending);
    assert(sortTitleDesc[0].getTitle() == "Yas");
    assert(sortTitleDesc[1].getTitle() == "Titanic");
    assert(sortTitleDesc[2].getTitle() == "Fast&Furious");
    assert(sortTitleDesc[3].getTitle() == "ABCD");
    assert(sortTitleDesc[4].getTitle() == "ABC");
}

void testSortMainChar(const MovieRent & srv) {
  const vector<Movie> sortMainCharAsc = srv.sorting(SortType::MainChar, SortOrder::Ascending);
    assert(sortMainCharAsc[0].getMainChar() == "Johnny Depp");
    assert(sortMainCharAsc[1].getMainChar() == "Leonardo DiCaprio");
    assert(sortMainCharAsc[2].getMainChar() == "Nicolas Cage");
    assert(sortMainCharAsc[3].getMainChar() == "Paul Walker");
    assert(sortMainCharAsc[4].getMainChar() == "Vin Diesel");

    const vector<Movie> sortMainCharDesc = srv.sorting(SortType::MainChar, SortOrder::Descending);
    assert(sortMainCharDesc[0].getMainChar() == "Vin Diesel");
    assert(sortMainCharDesc[1].getMainChar() == "Paul Walker");
    assert(sortMainCharDesc[2].getMainChar() == "Nicolas Cage");
    assert(sortMainCharDesc[3].getMainChar() == "Leonardo DiCaprio");
    assert(sortMainCharDesc[4].getMainChar() == "Johnny Depp");
}

void testSortGenreYear(const MovieRent & srv) {
  const vector<Movie> sortGenreYearAsc = srv.sorting(SortType::GenreYear, SortOrder::Ascending);
    assert(sortGenreYearAsc[0].getTitle() == "Titanic");

  const vector<Movie> sortGenreYearDesc = srv.sorting(SortType::GenreYear, SortOrder::Descending);
    assert(sortGenreYearDesc[0].getTitle() == "Yas");
}

void testInvalidSort() {
    MovieRepository repo;
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};

    srv.addMovie("Test", "Genre", year_2000, "Actor");

    bool exceptionThrown = false;
    try {
        vector<Movie> sort = srv.sorting(static_cast<SortType>(-1), SortOrder::Ascending);
    } catch (const RepoException&) {
        exceptionThrown = true;
    }
    assert(exceptionThrown);
}

void testingService2() {
    MovieRepository repo;
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};

    // setup
    srv.addMovie("Fast&Furious", "Action", year_2004, "Vin Diesel");
    srv.addMovie("Titanic", "Romance", year_1997, "Leonardo DiCaprio");
    srv.addMovie("ABC", "Romance", year_2000, "Nicolas Cage");
    srv.addMovie("Yas", "Drama", year_2005, "Paul Walker");
    srv.addMovie("ABCD", "Romance", year_2000, "Johnny Depp");
    assert(srv.getMovies().size() == 5);

    testFilterFunctions(srv);
    testSortTitle(srv);
    testSortMainChar(srv);
    testSortGenreYear(srv);
    testInvalidSort();
}

void test_shopping_cart() {
    ShoppingCart shoppingCart;
    assert(shoppingCart.getallShoppingCart().empty());

    // add to cart
    const Movie movie1("Fast&Furious","Action",year_2004,"Vin Diesel");
    shoppingCart.addToCart(movie1);
    assert(shoppingCart.getallShoppingCart().size() == 1);
    assert(shoppingCart.getallShoppingCart()[0].getTitle()=="Fast&Furious");

    // delete cart
    shoppingCart.deleteCart();
    assert(shoppingCart.getallShoppingCart().empty());

    // random cart
    const vector<Movie> movies = {Movie("Fast&Furious","Action",year_2004,"Vin Diesel"),
                            Movie("Titanic","Romance",year_1997,"Leonardo DiCaprio"),
                            Movie("Mystic River","Crime", year_2003,"Kevin Bacon")};

    shoppingCart.randomCart(2,movies);
    assert(shoppingCart.getallShoppingCart().size() == 2);

    shoppingCart.deleteCart();
    shoppingCart.randomCart(number_5,movies);
    assert(shoppingCart.getallShoppingCart().size() == 5);
}

void test_service_shopping_cart_add() {
    MovieRepository repo;
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};

    srv.addMovie("Fast&Furious", "Action", year_2004, "Vin Diesel");
    const vector<Movie> shopping_cart_init = srv.getAllCart();
    assert(shopping_cart_init.empty());
    const vector<Movie> shopping_cart = srv.addToCart("Fast&Furious");
    assert(shopping_cart.size() == 1);
    assert(shoppingCart.getallShoppingCart()[0].getTitle() == "Fast&Furious");

    try {
      (void)srv.addToCart("Fast&Furious");
    } catch (RepoException &) { assert(true);
    }

    const vector<Movie> delete_cart = srv.deleteCart();
    assert(delete_cart.empty());
}

void test_srv_random_cart() {
    MovieRepository repo;
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};

    srv.addMovie("Fast&Furious","Action",year_2004,"Vin Diesel");
    srv.addMovie("Titanic","Romance",year_1997,"Leonardo DiCaprio");
    srv.addMovie("ABC","Romance",year_2000," DiCaprio");
    srv.addMovie("Yas","Drama",year_2005,"Paul Walker");

    vector<Movie> random1 = srv.randomCart(2);
    assert(srv.getAllCart().size() == 2);
}

void test_export_csv () {
    MovieRepository repo;
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};

    srv.addMovie("Titanic", "Romantic", year_1997, "Leonardo DiCaprio");

    const vector<Movie>& movies = srv.randomCart(2);;
    MovieRent::exportCSV("testcsv.csv", movies);
    std::ifstream fin("testcsv.csv");
    string line;
    getline(fin, line);
    assert(line == "Titanic,Romantic,1997,Leonardo DiCaprio");
    fin.close();
    std::ofstream ofs("testcsv.csv", std::ios::trunc);
    ofs.close();
}

void test_srv_export_html() {
    MovieRepository repo;
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};

    srv.addMovie("The Godfather", "Drama", year_1972, "Marlon Brando");

    const vector<Movie>& movies = srv.randomCart(1);
    MovieRent::exportHTML("testhtml.html", movies);
    std::ifstream fin("testhtml.html");
    string line;
    getline(fin, line);
    assert(line == "<html><body>");
    getline(fin, line);
    assert(line == "<table border=\"1\" style=\"width:100 % \">");
    getline(fin, line);
    assert(line == "<tr>");
    getline(fin, line);
    assert(line == "<td>The Godfather</td>");
    getline(fin, line);
    assert(line == "<td>Drama</td>");
    getline(fin, line);
    assert(line == "<td>1972</td>");
    getline(fin, line);
    assert(line == "<td>Marlon Brando</td>");
    getline(fin, line);
    assert(line == "</tr>");
    getline(fin, line);
    assert(line == "</table>");
    getline(fin, line);
    assert(line == "</body></html>");
    fin.close();
    std::ofstream fout("testhtml.html", std::ios::trunc);
    fout.close();
}

void test_undo() {
    RepoFile repo{"movies-undo.txt"};
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};

    srv.addMovie("Titanic","Romance",year_1997,"Leonardo DiCaprio");
    assert(srv.getMovies().size() == 1);
    srv.updateMovie("Titanic","Action",year_2004,"Vin Diesel");
    assert(srv.getMovies().size() == 1);
    srv.deleteMovie("Titanic");
    assert(srv.getMovies().empty());

    srv.undo();
    assert(srv.getMovies().size() == 1);
    assert(repo.getMovies()[0].getTitle() == "Titanic");
    assert(repo.getMovies()[0].getGenre() == "Action");
    assert(repo.getMovies()[0].getYear() == year_2004);
    assert(repo.getMovies()[0].getMainChar() == "Vin Diesel");

    srv.undo();
    assert(srv.getMovies().size() == 1);
    assert(repo.getMovies()[0].getTitle() == "Titanic");
    assert(repo.getMovies()[0].getGenre() == "Romance");
    assert(repo.getMovies()[0].getYear() == year_1997);
    assert(repo.getMovies()[0].getMainChar() == "Leonardo DiCaprio");

    srv.undo();
    assert(srv.getMovies().empty());

}

void test_service() {
    testService();
    testingService2();
    test_service_shopping_cart_add();
    test_srv_random_cart();
    test_export_csv();
    test_srv_export_html();
    test_undo();
}

void testing() {
    testRepo();
    test_read_from_file();
    test_service();
    test_shopping_cart();
    std::cout << "All tests have passed!" << '\n';
}
