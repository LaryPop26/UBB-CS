#include <iostream>
#include <stdio.h>
#include <mpi.h>

using namespace std;
const int N=12;

void print(int* a, int n) {
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}
int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);
    int a[N];
    int b[N];
    int c[N];
    MPI_Status status;

    int rank, size;

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int dim = N / size;

    if (rank==0) {
        for ( int i=0; i<N; ++i) {
            a[i] = i;
            b[i] = i;
        }
    }
    auto startTime = MPI_Wtime();
    // N/P
    int* a_new = new int[dim];
    MPI_Scatter(a, dim, MPI_INT, a_new, dim, MPI_INT, 0, MPI_COMM_WORLD);

    int* b_new = new int[dim];
    MPI_Scatter(b, dim, MPI_INT, b_new, dim, MPI_INT, 0, MPI_COMM_WORLD);

    int* c_new = new int[dim];
    for (int i = 0; i < dim; ++i) {
        c_new[i] = a_new[i] + b_new[i];
    }

    MPI_Gather(c_new, dim, MPI_INT, c, dim, MPI_INT, 0, MPI_COMM_WORLD);

    auto endTime = MPI_Wtime();
    cout <<"Time: " <<endTime - startTime << " sec" << endl;
    if (rank==0) {
        print(c, N);
    }
    MPI_Finalize();
    return 0;
}