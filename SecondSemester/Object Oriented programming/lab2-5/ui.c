//
// Created by popla on 12-Mar-25.
//

#include <stdio.h>
#include <string.h>
#include "MyList.h"
#include "controller.h"
#include "entity.h"
#include "tests.h"

void printMenu() {
    printf("Programing contest Main Menu.\n");
    printf("1. Add participant\n");
    printf("2. Update participant\n");
    printf("3. Delete participant\n");
    printf("4. Filter participants\n");
    printf("5. Sort participants\n");
    printf("6. Show all participants\n");
    printf("7. Undo last operation (add/update/delete)\n");
    printf("0. Exit\n");
}

void filterMenu() {
    printf("Filter participants.\n");
    printf("1. Score under a value\n");
    printf("2. Lastname starting with a letter\n");
}

void sortMenu() {
    printf("Sort participants.\n");
    printf("1. Ascending names\n");
    printf("3. Ascending score\n");
}

void show(MyList* lst) {
    if (lst->length == 0) printf("No participants\n");
    for (int i=0; i<size(lst); i++) {
        Participant* p = getMyElement(lst, i);
        printf("%d. Name: %s %s | Score: %d\n",i+1,p->lastName, p->firstName, p->score);
    }
}

void addParticipantUI(ManagerParticipants* contest) {
    int score;
    char lastName[30], firstName[30];
    getchar();
    printf("Enter last name: ");
    fgets(lastName, 30, stdin);
    printf("Enter first name: ");
    fgets(firstName, 30, stdin);
    lastName[strcspn(lastName, "\n")] = 0;
    firstName[strcspn(firstName, "\n")] = 0;

    printf("Enter score: ");
    scanf("%d", &score);
    getchar();

    int successful = addParticipant(contest, lastName, firstName, score);
    if (successful) printf("Successfully added Participant\n");
    else printf("Error while adding participant\n");
}

void addDefault(ManagerParticipants* contest) {
    addParticipant(contest,"Ionescu", "Diana", 100);
    addParticipant(contest, "Dumitrescu", "Alex", 80);
    addParticipant(contest, "Stan", "Briana", 90);
    addParticipant(contest, "Iliescu", "George", 20);
    addParticipant(contest, "Barbu", "Ionela", 40);
    printf("\n ");
}

void updateParticipantUI(ManagerParticipants* contest) {
    int score;
    char lastName[30], firstName[30];
    getchar();
    printf("Enter last name: ");
    fgets(lastName, 30, stdin);
    lastName[strcspn(lastName, "\n")] = 0;
    printf("Enter first name: ");
    fgets(firstName, 30, stdin);
    firstName[strcspn(firstName, "\n")] = 0;

    printf("Enter score: ");
    scanf("%d", &score);
    getchar();

    int successful = updateParticipant(contest, lastName, firstName, score);
    if (successful) printf("Successfully updated Participant\n");
    else printf("Error while updating participant\n");
}

void deleteParticipantUI(ManagerParticipants* contest) {
    char lastName[30], firstName[30];
    getchar();
    printf("Enter last name: ");
    fgets(lastName, 30, stdin);
    lastName[strcspn(lastName, "\n")] = 0;
    printf("Enter first name: ");
    fgets(firstName, 30, stdin);
    firstName[strcspn(firstName, "\n")] = 0;

    int successful = deleteParticipant(contest, lastName, firstName);
    if (successful) printf("Successfully deleted Participant\n");
    else printf("Error while deleting participant\n");
}

void filterScoreUI(ManagerParticipants* manager) {
    int score;
    getchar();
    printf("Enter maximum score: ");
    scanf("%d", &score);
    MyList* filteredList = filterScore(manager, score);
    show(filteredList);
    destroyMyList(filteredList);
}

void filterFirstLetterUI(ManagerParticipants * manager) {
    char firstLetter[2];
    getchar();
    printf("Enter first letter: ");
    fgets(firstLetter, 2, stdin);
    firstLetter[strcspn(firstLetter, "\n")] = 0;
    MyList* filteredList = filterFirstLetter(manager, firstLetter);
    show(filteredList);
    destroyMyList(filteredList);
}

void sortByNameUI(ManagerParticipants* contest) {
    MyList* sortedList = sortByName(contest);
    show(sortedList);
    destroyMyList(sortedList);
}

void sortByScoreUI(ManagerParticipants* contest) {
    MyList* sortedList = sortByScore(contest);
    show(sortedList);
    destroyMyList(sortedList);
}

void undoUI(ManagerParticipants* contest) {
    int successful = undo(contest);
    if (successful) printf("Undo realised\n");
    else printf("Coudn't realise undo (list is empty)\n");
}

void run() {
    run_tests();
    int is_running = 1;
    ManagerParticipants contest = createManagerParticipants();
    addDefault(&contest);
    while (is_running) {
        printMenu();
        printf(">>>");
        short int cmd;
        scanf("%hd", &cmd);
        switch (cmd) {
            case 1:
                printf("Add participant\n");
                addParticipantUI(&contest);
                break;
            case 2:
                printf("Update participant\n");
                updateParticipantUI(&contest);
                break;
            case 3:
                printf("Delete participant\n");
                deleteParticipantUI(&contest);
                break;
            case 4:
                filterMenu();
                short int option1;
                printf(">>> ");
                scanf("%hd", &option1);
                switch (option1) {
                    case 1:
                        printf("Filter after score\n");
                        filterScoreUI(&contest);
                        break;
                    case 2:
                        printf("Filter after first letter\n");
                        filterFirstLetterUI(&contest);
                        break;
                    default:
                        break;
                }
                break;
            case 5:
                sortMenu();
                short int option2;
                printf(">>> ");
                scanf("%hd", &option2);
                switch (option2) {
                    case 1:
                        printf("Sort ascending names\n");
                        sortByNameUI(&contest);
                        break;
                    case 2:
                        printf("Sort ascending scores\n");
                        sortByScoreUI(&contest);
                        break;
                    default:
                        break;
                }
                break;
            case 6:
                printf("List of participants: \n");
                show(contest.lstParticipants);
                break;
            case 7:
                undoUI(&contest);
                break;
            case 0:
                is_running = 0;
                destroyManagerParticipants(&contest);
                break;
            default:
                printf("Invalid command\n");
                break;
        }
    }
}

int main(void) {
    run();
    
}
