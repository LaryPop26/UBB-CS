//
// Created by popla on 12-Mar-25.
//

#include "ui.h"
#include <stdio.h>
#include <string.h>
#include "MyList.h"

void printMenu() {
    printf("Programing contest Main Menu.\n");
    printf("1. Add participant\n");
    printf("2. Update participant\n");
    printf("3. Delete participant\n");
    printf("4. Filter participants\n");
    printf("5. Sort participants\n");
    printf("6. Show all participants\n");
    printf("7. Exit\n");
}

void filterMenu() {
    printf("Filter participants.\n");
    printf("1. Score under a value\n");
    printf("2. Lastname starting with a letter\n");
}

void sortMenu() {
    printf("Sort participants.\n");
    printf("1. Ascending names\n");
    printf("2. Descending names\n");
    printf("3. Ascending score\n");
    printf("4. Descending score\n");
}

void show(MyList* participants) {
    if (size(participants) == 0) printf("No participants\n");
    for (int i=0; i<size(participants); i++) {
        Participant p = getMyElement(participants, i);
        printf("%d. Name: %s %s | Score: %d\n",i+1,p.lastName, p.firstName, p.score);
    }
}

void addParticipantUI(MyList* participants) {
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
    scanf_s("%d", &score);
    getchar();

    int errorCode = addParticipantController(participants, lastName, firstName, score);
    if (errorCode != 0) printf("Error while adding participant\n");
    else printf("Successfully added Participant\n");
}

void addDefault(MyList* participants) {
    addParticipantController(participants,"Ionescu", "Diana", 100);
    addParticipantController(participants, "Dumitrescu", "Alex", 80);
    addParticipantController(participants, "Stan", "Briana", 90);
    addParticipantController(participants, "Iliescu", "George", 20);
    addParticipantController(participants, "Barbu", "Ionela", 40);
    printf("\n ");
}

void updateParticipantUI(MyList *participants) {
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
    scanf_s("%d", &score);
    getchar();

    int errorCode = updateParticipantController(participants, lastName, firstName, score);
    if (errorCode != 0) printf("Error while modifing participant\n");
    else printf("Successfully modified Participant\n");
}

void deleteParticipantUI(MyList *participants) {
    int poz;
    printf("Enter position to be deleted: ");
    scanf_s("%d", &poz);

    int errorCode = deleteParticipantController(participants, poz-1);
    if (errorCode != 0) printf("Error while deleting participant\n");
    else printf("Successfully deleted Participant\n");
}

void filterScoreUI(MyList* participants) {
    int score;
    printf("Enter maximum score: ");
    scanf_s("%d", &score);
    MyList filteredList = filterScore(participants, score);
    show(&filteredList);
}

void filterFirstLetterUI(MyList * participants) {
    char firstLetter[2];
    getchar();
    printf("Enter first letter: ");
    fgets(firstLetter, 2, stdin);
    firstLetter[strcspn(firstLetter, "\n")] = 0;
    MyList filteredList = filterFirstLetter(participants, firstLetter);
    show(&filteredList);
}


void run() {
    run_tests();
    bool is_running = true;
    MyList participants = createEmpty();
    addDefault(&participants);
    while (is_running) {
        printMenu();
        printf(">>>");
        short int cmd;
        scanf_s("%hd", &cmd);
        switch (cmd) {
            case 1:
                printf("Add participant\n");
                addParticipantUI(&participants);
                break;
            case 2:
                printf("Update participant\n");
                updateParticipantUI(&participants);
                break;
            case 3:
                printf("Delete participant\n");
                deleteParticipantUI(&participants);
                break;
            case 4:
                filterMenu();
                short int option1;
                printf(">>> ");
                scanf_s("%hd", &option1);
                switch (option1) {
                    case 1:
                        printf("Filter after score\n");
                        filterScoreUI(&participants);
                        break;
                    case 2:
                        printf("Filter after first letter\n");
                        filterFirstLetterUI(&participants);
                        break;
                    default:
                        break;
                }
                break;
            case 5:
                sortMenu();
                short int option2;
                printf(">>> ");
                scanf_s("%hd", &option2);
                switch (option2) {
                    case 1:
                        printf("sort1\n");
                        break;
                    case 2:
                        printf("sort2\n");
                        break;
                    case 3:
                        printf("sort3\n");
                        break;
                    case 4:
                        printf("sort4\n");
                        break;
                    default:
                        break;
                }
                break;
            case 6:
                printf("List of participants: \n");
                show(&participants);
                break;
            case 7:
                is_running = false;
                break;
            default:
                printf("Invalid command\n");
                break;
        }
    }
}
