#include <iostream>
#include <stdio.h>
#include <mpi.h>
#include <sec_api/string_s.h>

using namespace std;

int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);

    int rank, size;

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank==0) {
        char helloStr[20];
        char globalHello[200];
        MPI_Status status;

        sprintf_s(globalHello,20, "Hello from %d\n", 0);

        for (int i = 1; i < size; i++) {
            MPI_Recv(helloStr, 20, MPI_CHAR, i, 0, MPI_COMM_WORLD, &status);

            // sprintf_s(globalHello + i * 20, 20, helloStr);
            strcat_s(globalHello, helloStr);
        }

        cout << globalHello << '\n';
    }
    else {
        char hello[20];

        sprintf_s(hello,20, "Hello from %d\n", rank);
        MPI_Send(hello, 20, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
    }

    MPI_Finalize();
    return 0;
}